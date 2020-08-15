from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import create_access_token
from sqlalchemy.sql import func
from dataclasses import dataclass
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()


@dataclass
class User(db.Model, UserMixin):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str
    hashed_password: str
    bio: str
    profile_pic_url: str

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    hashed_password = db.Column(db.String(128))
    bio = db.Column(db.Text, nullable=True)
    profile_pic_url = db.Column(db.String(255), nullable=True)

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_token(self):
        return create_access_token(identity=self.email)

    def to_dict(self):
        return {'id': self.id, 'username': self.username, 'email': self.email, 'first_name': self.first_name, 'last_name': self.last_name, 'bio': self.bio, 'profile_pic_url': self.profile_pic_url}

    user_hikes = db.relationship('UserHike', back_populates='user')
    post = db.relationship('Post', back_populates='user')
    like = db.relationship('Like', back_populates='user')
    comment = db.relationship('Comment', back_populates='user')


@dataclass
class Location(db.Model):
    id: int
    name: str
    city: str
    state: str
    country: str
    description: str

    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)

    user_hikes = db.relationship('UserHike', back_populates='location')
    post = db.relationship('Post', back_populates='location')

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'city': self.city, 'state': self.state, 'country': self.country, 'description': self.description}


@dataclass
class UserHike(db.Model):
    id: int
    user: User
    location: Location

    __tablename__ = 'user_hikes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey(
        'locations.id'), nullable=False)

    user = db.relationship('User', back_populates='user_hikes')
    location = db.relationship('Location', back_populates='user_hikes')

    def to_dict(self):
        return {'id': self.id, 'user_id': self.user_id, 'location_id': self.location_id}


@dataclass
class Post(db.Model):
    id: int
    user: User
    location: Location
    title: str
    text: str
    photo_url: str

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey(
        'locations.id'), nullable=True)
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    user = db.relationship('User', back_populates='post')
    location = db.relationship('Location', back_populates='post')
    like = db.relationship('Like', back_populates='post')
    comment = db.relationship('Comment', back_populates='post')


@dataclass
class Like(db.Model):
    id: int
    user_id: int
    post_id: int

    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)

    user = db.relationship('User', back_populates='like')
    post = db.relationship('Post', back_populates='like')


@dataclass
class Comment(db.Model):
    id: int
    user_id: int
    post_id: int
    comment: str

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    comment = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    user = db.relationship('User', back_populates='comment')
    post = db.relationship('Post', back_populates='comment')
