from flask import jsonify, Blueprint

blueprint3 = Blueprint('hack3', __name__)

@blueprint3.route('/hack3', methods=['DELETE'])
def hack3():
    return jsonify({'payload': 'success'}), 200