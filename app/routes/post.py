from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.config import S3_BUCKET
import boto3
from app.models import db, Post, User, Comment, Like, Follow
from sqlalchemy import and_


bp = Blueprint('post', __name__, url_prefix='/api/posts')

# user makes a post


@bp.route('/user/<int:id>', methods=['POST'])
@jwt_required
def make_post(id):
    current_user = get_jwt_identity()
    if current_user != id:
        return jsonify({'message': 'Unauthorized user!'}), 401
    data = request.form

    if request.files:
        file = request.files["image"]
        s3_resource = boto3.resource('s3')
        my_bucket = s3_resource.Bucket(S3_BUCKET)
        my_bucket.Object(file.filename).put(
            Body=file, ACL='public-read')

    if data['location'] == 'None':
        new_post = {
            'user_id': id,
            'text': data['text'],
            'title': data['title'],
        }
    else:
        new_post = {
            'user_id': id,
            'location_id': data['location'],
            'text': data['text'],
            'title': data['title'],
        }

    if request.files:
        new_post[
            'photo_url'] = f'https://{S3_BUCKET}.s3-us-west-2.amazonaws.com/{my_bucket.Object(file.filename).key}'

    post = Post(**new_post)

    db.session.add(post)
    db.session.commit()
    print('--------POST WAS ADDED--------')
    return jsonify(post)

# get a post


@ bp.route('/<int:id>')
def get_post(id):
    post_query = Post.query.filter(Post.id == id).all()
    print('------QUERYING FOR POST------')
    post = {'id': post_query[0].id, 'text': post_query[0].text,
            'title': post_query[0].title, 'username': post_query[0].user.username}
    return jsonify(post)


# delete a post


@ bp.route('/<int:id>', methods=['DELETE'])
@ jwt_required
def delete_post(id):
    current_user = get_jwt_identity()
    post = Post.query.filter(Post.id == id).all()
    if current_user != post[0].user_id:
        return jsonify({'message': 'You are not authorized to delete this post!'}), 401
    db.session.delete(post[0])
    db.session.commit()
    print('--------POST DELETED------')
    return jsonify(post)

# update a post


@ bp.route('/<int:post_id>/user/<int:user_id>', methods=['PUT'])
@ jwt_required
def update_post(post_id, user_id):
    data = request.get_json()
    current_user = get_jwt_identity()
    if current_user != user_id:
        return jsonify({'message': 'Unauthorized user!'}), 401
    post = Post.query.filter(Post.id == post_id).all()
    post[0].title = data['title']
    post[0].text = data['text']
    db.session.commit()
    print('----POST WAS UPDATED------')
    updated_post = {'id': post[0].id, 'text': post[0].text,
                    'title': post[0].title, 'username': post[0].user.username}
    return jsonify(updated_post)


# get all posts for a user
@ bp.route('/user/<int:id>')
@ jwt_required
def get_posts(id):
    current_user = get_jwt_identity()
    posts = Post.query.filter(Post.user_id == id).all()

    def sorted_posts(e):
        return e['created_at']

    print('-----QUERYING DATABASE------')
    liked_posts = [
        post.like[0].post_id for post in posts if post.like and post.like[0].user_id == current_user]

    posts = [{'id': post.id, 'profile_pic': post.user.profile_pic_url, 'username': post.user.username, 'title': post.title, 'text': post.text,
              'photo_url': post.photo_url, 'location': post.location.name if post.location else None, 'comments': [{'id': comment.id, 'comment': comment.comment, 'username': comment.user.username} for comment in post.comment], 'created_at': post.created_at} for post in posts]
    posts.sort(key=sorted_posts, reverse=True)
    return jsonify({'liked_posts': liked_posts, 'posts': posts})

# get a users feed


@bp.route('/feed')
@jwt_required
def get_feed():
    current_user = get_jwt_identity()

    def sorted_posts(e):
        return e['created_at']
    posts = Post.query.filter().all()
    print('-----QUERYING DATABASE------')
    liked_posts = [
        post.like[0].post_id for post in posts if post.like and post.like[0].user_id == current_user]

    posts = [{'id': post.id, 'profile_pic': post.user.profile_pic_url, 'username': post.user.username, 'title': post.title, 'text': post.text,
              'photo_url': post.photo_url, 'location': post.location.name if post.location else None, 'comments': [{'id': comment.id, 'comment': comment.comment, 'username': comment.user.username} for comment in post.comment], 'created_at': post.created_at} for post in posts]
    posts.sort(key=sorted_posts, reverse=True)
    return jsonify({'liked_posts': liked_posts, 'posts': posts})


# make a comment on a post
@ bp.route('/<int:post_id>/user/<int:user_id>/comment', methods=['POST'])
@ jwt_required
def make_comment(post_id, user_id):
    current_user = get_jwt_identity()
    if current_user != user_id:
        return jsonify({'message': 'Unauthorized user!'}), 401
    data = request.get_json()

    new_comment = {
        'user_id': user_id,
        'post_id': post_id,
        **data
    }

    comment = Comment(**new_comment)

    db.session.add(comment)
    db.session.commit()
    print('-------NEW COMMENT-------')
    return jsonify(comment)

# like a post


@ bp.route('/<int:post_id>/like', methods=['POST'])
@ jwt_required
def make_like(post_id):
    current_user = get_jwt_identity()
    existing_like = Like.query.filter(
        and_(Like.post_id == post_id, Like.user_id == current_user)).all()
    if existing_like:
        return jsonify({'message': 'Like already exists!'})

    new_like = {
        'user_id': current_user,
        'post_id': post_id
    }

    like = Like(**new_like)

    db.session.add(like)
    db.session.commit()
    print('------NEW LIKE-------')
    return jsonify(like)

# delete a like


@ bp.route('/<int:post_id>/like', methods=['DELETE'])
@ jwt_required
def delete_like(post_id):
    current_user = get_jwt_identity()
    like = Like.query.filter(
        and_(Like.post_id == post_id, Like.user_id == current_user)).all()
    db.session.delete(like[0])
    db.session.commit()
    print('-------LIKE DELETED-----')
    return jsonify(like)
