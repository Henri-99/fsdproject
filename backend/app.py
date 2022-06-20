from flask import Flask, jsonify
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate app
app = Flask(__name__)
app.config.from_object(__name__)

# enable Cross-Origin Resource Sharing
CORS(app, resources={r'/*': {'origins': '*'}})

# testing route
@app.route('/ping', methods=['GET'])
def ping_pong():
	return jsonify('pong!')



if __name__ == '__main__':
	app.run()