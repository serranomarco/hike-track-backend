from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db, Post, User, Comment


bp = Blueprint('post', __name__, url_prefix='/api/posts')

# user makes a post


@bp.route('/user/<int:id>', methods=['POST'])
@jwt_required
def make_post(id):
    current_user = get_jwt_identity()
    print('THIS IS THE CURRENT USER:')
    print(current_user)
    if current_user != id:
        return jsonify({'message': 'Unauthorized user!'}), 401
    data = request.get_json()
    print(data)

    new_post = {
        'user_id': id,
        **data
    }

    post = Post(**new_post)

    db.session.add(post)
    db.session.commit()
    print('--------POST WAS ADDED--------')
    return jsonify(post)

# get a post


@bp.route('/<int:id>')
def get_post(id):
    post_query = Post.query.filter(Post.id == id).all()
    print('------QUERYING FOR POST------')
    post = {'id': post_query[0].id, 'text': post_query[0].text,
            'title': post_query[0].title, 'username': post_query[0].user.username}
    return jsonify(post)

# update a post


@bp.route('/<int:post_id>/user/<int:user_id>', methods=['PUT'])
@jwt_required
def update_post(post_id, user_id):
    data = request.get_json()
    current_user = get_jwt_identity()
    print('THIS IS THE CURRENT USER:')
    print(current_user)
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
    print('THIS IS THE CURRENT USER:')
    print(current_user)
    if current_user != id:
        return jsonify({'message': 'Unauthorized user!'}), 401
    posts = Post.query.filter(Post.user_id == id).all()

    def sorted_posts(e):
        return e['created_at']

    print('-----QUERYING DATABASE------')
    posts = [{'id': post.id, 'username': post.user.username, 'title': post.title, 'text': post.text,
              'photo_url': post.photo_url, 'created_at': post.created_at} for post in posts]
    posts.sort(key=sorted_posts, reverse=True)
    print(posts)
    return jsonify(posts)


# make a comment on a post
@ bp.route('/<int:post_id>/user/<int:user_id>/comment', methods=['POST'])
@ jwt_required
def make_comment(post_id, user_id):
    current_user = get_jwt_identity()
    print('THIS IS THE CURRENT USER:')
    print(current_user)
    if current_user != id:
        return jsonify({'message': 'Unauthorized user!'}), 401
    data = request.get_json()
    print(data)

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
