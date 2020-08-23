from flask import Blueprint, jsonify, request
from app.models import db, Post, User


bp = Blueprint('post', __name__, url_prefix='/api/posts')


@bp.route('/user/<int:id>', methods=['POST'])
def make_post(id):
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


@bp.route('/user/<int:id>')
def get_posts(id):
    posts = Post.query.filter(Post.user_id == id).all()

    def sorted_posts(e):
        return e['created_at']

    print('-----QUERYING DATABASE------')
    posts = [{'id': post.id, 'username': post.user.username, 'title': post.title, 'text': post.text,
              'photo_url': post.photo_url, 'created_at': post.created_at} for post in posts]
    posts.sort(key=sorted_posts, reverse=True)
    print(posts)
    return jsonify(posts)
