from flask import Blueprint, jsonify, request

class Alluser:
    def __init__(self, blueprint):
        self.blueprint = blueprint


    def register_route(self):
        self.blueprint.route('/users', methods=['GET'])(self.getter)
        self.blueprint.route('/user', methods=['POST'])(self.poster)
        self.blueprint.route('/user', methods=['DELETE'])(self.delete)
        self.blueprint.route('/user', methods=['PUT'])(self.puts)
        self.blueprint.route('/api/v1/users', methods=['GET'])(self.getlist)
        self.blueprint.route('/api/v1/user/', methods=['POST'])(self.postlist)
        self.blueprint.route('/api/v1/user/add', methods=['POST'])(self.postagain)
        self.blueprint.route('/api/v1/user/create', methods=['POST'])(self.create_user)
        return self.blueprint
        

    """HACK 1"""
    def getter(self):
        if request.method == 'GET':
            return jsonify({'payload': 'success'}), 200
        else:
            return jsonify({'error': 'It is Invalid Request'}), 405

    """HACK 2"""
    def poster(self):
        if request.method == 'POST':
            return jsonify({'payload': 'success'}), 200
        else:
            return jsonify({'error': 'It is Invalid Request'}), 405
    
    """HACK 3"""
    def delete(self):
        if request.method == 'DELETE':
            return jsonify({'payload': 'success'}), 200
        else:
            return jsonify({'error': 'It is Invalid Request'}), 405
        
    """HACK 4"""
    def puts(self):
        if request.method == 'PUT':
            return jsonify({'payload': 'success', 'error': False}), 200
        else:
            return jsonify({'error': 'It is Invalid Request'}), 405
        
    """HACK 5"""
    def getlist(self):
        if request.method == 'GET':
            return jsonify({'payload': []}), 200
        else:
            return jsonify({'error': 'It is Invalid Request'}), 405
        
    """HACK 6"""
    """POR RESOLVER"""
    def postlist(self):
        if request.method == 'POST':
            try:
                email = request.args['email']
                name = request.args['name']
                if email and name:
                    return jsonify({'payload': {'name': name, 'email': email}}), 200
                else:
                    return jsonify({'error': 'error'}), 405
            except Exception as e:
                return jsonify({'error': str(e)}),500
            
    """HACK 7"""
    def postagain(self):
        if request.method == 'POST':
            try:
                email = request.form.get('email')
                name = request.form.get('name')
                id = request.form.get('id')
                if email and name and id:
                    return jsonify({'payload' : {'email': email,'name': name,'id': id }}), 200
                else:
                    return jsonify({
                        'error': 'error'
                        }),405
            except Exception as e:
                return jsonify({
                        'error': str(e)
                    }), 500

    """HACK 8"""
    def create_user(self):
        try:
            data = request.get_json()
            email = data["email"]
            name = data["name"]
            id = data["id"]
            return jsonify({'payload': {'email':email, 'name':name, 'id':id }}), 200
        except Exception as e:
            error_response = {
               'error': str(e)
         }
            return jsonify(error_response), 400
        