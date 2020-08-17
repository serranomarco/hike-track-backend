from flask import Blueprint, jsonify, request
from app.models import db, Post


bp = Blueprint('post', __name__, url_prefix='/api/posts')


@bp.route('/user/<int:id>', method=['POST'])
def make_post(id):
    data = request.get_json()
    print(data)

    new_post = {
        'id': len(Post.query.all()) + 1,
        'user_id': id,
        'location_id': data['locationId'],
        'title': data['title'],
        'text': data['text'],
        'photo_url': data['photoUrl']
    }

    post = Post(**new_post)

    db.session.add(post)
    db.session.commit()
    print('--------POST WAS ADDED--------')
    return post
