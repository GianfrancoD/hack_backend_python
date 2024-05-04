from flask import Blueprint, jsonify

blueprint2 = Blueprint('hack2', __name__)

@blueprint2.route('/hack2', methods=['POST'])
def hack2():
    return jsonify({'payload':'success'}), 200
