from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db, User


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
        'profile_pic_url': 'default'
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

# get a user's profile


@bp.route('/user')
@jwt_required
def get_user():
    user = get_jwt_identity()
    user_info = User.query.filter(User.id == user).one()
    print('-----GETTING USER INFO-------')
    return {'username': user_info.username, 'profile_pic_url': user_info.profile_pic_url, 'bio': user_info.bio, 'first_name': user_info.first_name, 'last_name': user_info.last_name}
