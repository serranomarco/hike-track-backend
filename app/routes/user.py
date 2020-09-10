from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.config import S3_BUCKET
import boto3
from app.models import db, User, Follow
from sqlalchemy import and_


bp = Blueprint('user', __name__, url_prefix='/api/users')

# Register a user


@bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()

    email = User.query.filter(User.email == data['email']).all()
    username = User.query.filter(User.username == data['username']).all()

    if email or username:
        return {'error': 'User already exists'}

    new_user = {
        'id': len(User.query.all()) + 1,
        'username': data['username'],
        'first_name': data['firstName'],
        'last_name': data['lastName'],
        'email': data['email'],
        'profile_pic_url': 'https://hike-track-app.s3-us-west-2.amazonaws.com/default-profile.jpg'
    }

    user = User(**new_user)
    user.set_password = data['password']

    print('-------USER WAS ADDED------')

    db.session.add(user)
    db.session.commit()
    return {'token': user.get_token(), 'username': user.username, 'id': user.id}, 201

# login a user


@bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data['email']
    password = data['password']

    try:
        user = User.query.filter(User.email == email).one()
        print('---------LOGGING IN--------')
        return {'token': user.get_token(), 'username': user.username, 'id': user.id} if user.check_password(password) else {'error': 'Login failed'}
    except:
        return {'error': 'User was not found!'}

# get a current user's profile


@bp.route('/user')
@jwt_required
def get_user():
    user = get_jwt_identity()
    print(user)
    user_info = User.query.filter(User.id == user).one()
    following = Follow.query.filter(Follow.follower_id == user).all()
    followers = Follow.query.filter(Follow.following_id == user).all()

    print('-----GETTING USER INFO-------')
    return {'username': user_info.username, 'email': user_info.email, 'profile_pic_url': user_info.profile_pic_url, 'bio': user_info.bio, 'first_name': user_info.first_name, 'last_name': user_info.last_name, 'followers': [{'id': follower.id} for follower in followers], 'following': [{'id': follow.id} for follow in following]}

# update user profile


@bp.route('/user', methods=['PUT'])
@jwt_required
def update_user():
    data = request.get_json()
    user_id = get_jwt_identity()
    user = User.query.filter(User.id == user_id).one()
    print('-----QUERYING USER------')
    user.first_name = data['first_name']
    user.last_name = data['last_name']
    user.bio = data['bio']
    db.session.commit()
    print('-------UPDATING USER------')
    return {'username': user.username, 'email': user.email, 'profile_pic_url': user.profile_pic_url, 'bio': user.bio, 'first_name': user.first_name, 'last_name': user.last_name}


# update profile pic
@bp.route('/user/picture', methods=['PUT'])
@jwt_required
def update_profile_pic():
    user_id = get_jwt_identity()
    user = User.query.filter(User.id == user_id).one()
    print('--------QUERYING USER------')
    file = request.files["image"]
    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket(S3_BUCKET)
    my_bucket.Object(file.filename).put(
        Body=file, ACL='public-read')
    user.profile_pic_url = f'https://{S3_BUCKET}.s3-us-west-2.amazonaws.com/{my_bucket.Object(file.filename).key}'
    db.session.commit()
    print('----UPDATING PROFILE PIC------')
    return {'profile_pic_url': user.profile_pic_url}


# search for users
@bp.route('/search', methods=['POST'])
@jwt_required
def search_users():
    data = request.get_json()
    user_id = get_jwt_identity()
    input = data['search']
    search = '%{}%'.format(input)
    users = User.query.filter(
        and_(User.username.like(search), User.id != user_id)).all()
    print('-----SEARCHING USERS------')
    users = [{'username': user.username, 'profile_pic_url': user.profile_pic_url,
              'bio': user.bio, 'first_name': user.first_name, 'last_name': user.last_name} for user in users]
    return jsonify(users)

# get a users


@bp.route('/<username>')
@jwt_required
def get_all_users(username):
    user_id = get_jwt_identity()
    user = User.query.filter(User.username == username).one()
    print(user)
    following = Follow.query.filter(Follow.follower_id == user.id).all()
    followers = Follow.query.filter(Follow.following_id == user.id).all()
    user = User.query.filter(
        and_(User.id != user_id, User.username == username)).one()
    print('-----GETTING USER------')
    user = {'id': user.id, 'username': user.username, 'profile_pic_url': user.profile_pic_url,
            'bio': user.bio, 'first_name': user.first_name, 'last_name': user.last_name, 'followers': [{'id': follower.id} for follower in followers], 'following': [{'id': follow.id} for follow in following]}
    return jsonify(user)


# follow a user
@bp.route('/<int:id>/follow', methods=['POST'])
@jwt_required
def follow_user(id):
    user_id = get_jwt_identity()

    existing_follow = Follow.query.filter(
        and_(Follow.following_id == id, Follow.follower_id == user_id)).all()

    if existing_follow:
        return {'message': 'follow already exists!'}

    new_follow = {
        'follower_id': user_id,
        'following_id': id
    }

    print('-----FOLLOWING USER-----')
    follow = Follow(**new_follow)
    db.session.add(follow)
    db.session.commit()
    return {'follower_id': follow.follower_id, 'following_id': follow.following_id}


# delete a follow
@bp.route('/<int:id>/follow', methods=['DELETE'])
@jwt_required
def delete_follow(id):
    user_id = get_jwt_identity()

    follow = Follow.query.filter(
        and_(Follow.following_id == id, Follow.follower_id == user_id)).all()
    db.session.delete(follow[0])
    db.session.commit()
    print('-------LIKE DELETED-----')
    return {'message': 'like deleted'}

# get a follow


@bp.route('/<int:id>/follow')
@jwt_required
def get_follow(id):
    user_id = get_jwt_identity()

    existing_follow = Follow.query.filter(
        and_(Follow.following_id == id, Follow.follower_id == user_id)).all()

    if existing_follow:
        return {'message': 'follow already exists!'}

    return {'error': 'like does not exist'}
