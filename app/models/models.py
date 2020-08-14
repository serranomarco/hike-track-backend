from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import create_access_token
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
