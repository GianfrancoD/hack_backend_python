from flask import Blueprint, jsonify, request

class Alluser:
    def __init__(self, blueprint):
        self.blueprint = blueprint


    def getter(self):
        if request.method == 'GET':
            return jsonify({'payload': 'success'}), 200
        else:
            return jsonify({'error': 'It is Invalid Request'}), 405
        
    def register_route(self):
        self.blueprint.route('/users', methods=['GET'])(self.getter)
        return self.blueprint

    