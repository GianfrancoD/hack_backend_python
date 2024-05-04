from flask import Blueprint, jsonify, request

class Alluser:
    def __init__(self, blueprint):
        self.blueprint = blueprint

    def register_route(self):
        self.blueprint.route('/users', methods=['GET'])(self.getter)
        self.blueprint.route('/user', methods=['POST'])(self.poster)
        self.blueprint.route('/user', methods=['DELETE'])(self.delete)
        self.blueprint.route('/user', methods=['PUT'])(self.puts)
        return self.blueprint

    def getter(self):
        if request.method == 'GET':
            return jsonify({'payload': 'success'}), 200
        else:
            return jsonify({'error': 'It is Invalid Request'}), 405

    def poster(self):
        if request.method == 'POST':
            return jsonify({'payload': 'success'}), 200
        else:
            return jsonify({'error': 'It is Invalid Request'}), 405
    
    def delete(self):
        if request.method == 'DELETE':
            return jsonify({'payload': 'success'}), 200
        else:
            return jsonify({'error': 'It is Invalid Request'}), 405
        
    def puts(self):
        if request.method == 'PUT':
            return jsonify({'payload': 'success', 'error': False}), 200
        else:
            return jsonify({'error': 'It is Invalid Request'}), 405