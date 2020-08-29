from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db, Location


bp = Blueprint('location', __name__, url_prefix='/api/locations', )

# Create a location


@bp.route('/', methods=['POST'], strict_slashes=False)
@jwt_required
def make_location():
    print('in here')
    data = request.get_json()
    new_location = {
        'name': data['name'],
        'city': data['city'],
        'state': data['state'],
        'country': data['country'],
        'description': data['description'],
        'latitude': data['latitude'],
        'longitude': data['longitude']
    }

    location = Location(**new_location)

    db.session.add(location)
    db.session.commit()

    print('------ADDED A LOCATION------')
    return jsonify(location)

# get all location


@bp.route('/', strict_slashes=False)
@jwt_required
def get_locations():
    locations = Location.query.all()
    return jsonify(locations)
