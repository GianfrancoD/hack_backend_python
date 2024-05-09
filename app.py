from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# hack 1
@app.route('/users', methods=['GET'])
def getter():
        if request.method == 'GET':
            return jsonify({'payload': 'success'}), 200
        else:
            return jsonify({'error': 'It is Invalid Request'}), 405

# hack 2
@app.route('/user', methods=['POST'])
def poster():
        if request.method == 'POST':
            return jsonify({'payload': 'success'}), 200
        else:
            return jsonify({'error': 'It is Invalid Request'}), 405
        
# hack 3
@app.route('/user', methods=['DELETE'])
def delete():
    if request.method == 'DELETE':
        return jsonify({'payload': 'success'}), 200
    else:
        return jsonify({'error': 'It is Invalid Request'}), 405
    
# hack 4
@app.route('/user', methods=['PUT'])
def puts():
    if request.method == 'PUT':
        return jsonify({'payload': 'success', 'error': False}), 200
    else:
        return jsonify({'error': 'It is Invalid Request'}), 405
    
# hack 5
@app.route('/api/v1/users', methods=['GET'])
def getlist():
    if request.method == 'GET':
        return jsonify({'payload': []}), 200
    else:
        return jsonify({'error': 'It is Invalid Request'}), 405
        
# hack 6 [Por resolver]
@app.route('/api/v1/user', methods=['POST']) 
def postlist():
    if request.method == 'POST':
        try:
            email = request.args.get('email')
            name = request.args.get('name')
            if email and name:
                return jsonify({'payload': {'name': name, 'email': email}}), 200
            else:
                return jsonify({'error': 'error'}), 400
        except Exception as e:
            return jsonify({'error': str(e)}),500

# hack 7
@app.route('/api/v1/user/add', methods=['POST'])
def postagain():
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

# hack 8
@app.route('/api/v1/user/create', methods=['POST'])
def create_user():
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
    
if __name__ == "__main__":
    app.run(debug=True)