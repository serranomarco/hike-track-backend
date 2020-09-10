from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS
from app.config import Config, S3_KEY, S3_SECRET
from app.models import db
from .routes import index, user, post, location, files
import boto3

s3 = boto3.client(
    's3',
    aws_access_key_id=S3_KEY,
    aws_secret_access_key=S3_SECRET)

app = Flask(__name__)
app.config.from_object(Config)
jwt = JWTManager(app)
CORS(app)
db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(index.bp)
app.register_blueprint(user.bp)
app.register_blueprint(post.bp)
app.register_blueprint(location.bp)
app.register_blueprint(files.bp)
