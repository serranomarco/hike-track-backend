from os import environ


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL')
    SECRET_KEY = environ.get('SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = 108000


S3_BUCKET = environ.get('S3_BUCKET')
S3_KEY = environ.get('AWS_ACCESS_KEY_ID')
S3_SECRET = environ.get('AWS_SECRET_ACCESS_KEY')
