from flask import Blueprint, jsonify, request
from app.models import db, User


bp = Blueprint('user', __name__, url_prefix='/api/users')

# Register a user


@bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    print(data)

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
    print(user)

    db.session.add(user)
    db.session.commit()
    return {'token': user.get_token(), 'username': user.username, 'id': user.id}, 201


@bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    print(data)
    email = data['email']
    password = data['password']

    try:
        user = User.query.filter(User.email == email).one()
        print('---------LOGGING IN--------')
        return {'token': user.get_token(), 'username': user.username, 'id': user.id} if user.check_password(password) else {'error': 'Login failed'}
    except:
        return {'error': 'user was not found'}
