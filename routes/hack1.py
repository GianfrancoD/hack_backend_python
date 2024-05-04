from flask import Blueprint, jsonify

blueprint = Blueprint('hack1', __name__)

@blueprint.route('/hack1', methods=['GET'])
def hack1():
    return jsonify({'payload': 'success'}), 200