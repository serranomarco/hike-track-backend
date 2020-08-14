from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS
from app.config import Config
from app.models import db
from .routes import index, user

app = Flask(__name__)
app.config.from_object(Config)
jwt = JWTManager(app)
CORS(app)
db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(index.bp)
app.register_blueprint(user.bp)
