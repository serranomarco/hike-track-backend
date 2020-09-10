from flask import Blueprint, jsonify, request
from app.config import S3_BUCKET
import boto3


bp = Blueprint('files', __name__, url_prefix='/api/files')


# lets me know s3 is working
@bp.route('/')
def files():
    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket(S3_BUCKET)
    summaries = my_bucket.objects.all()
    for o in summaries:
        print(o.key)
    return {'message': 'bucket was read successfully'}, 200


@bp.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']

    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket(S3_BUCKET)
    my_bucket.Object(file.filename).put(Body=file)
    print(my_bucket.Object(file.filename).e_tag)

    return {'message': 'file was uploaded'}
