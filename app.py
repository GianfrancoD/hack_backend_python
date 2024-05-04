from flask import Flask, jsonify, request
from flask_cors import CORS
from routes.hack1 import *


app = Flask(__name__)
CORS(app)

users = Blueprint('users', __name__)
all_users = Alluser(users)

app.register_blueprint(all_users.register_route())

    
if __name__ == "__main__":
    app.run(debug=True)