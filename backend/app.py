from flask import Flask, jsonify, request
from flask_cors import CORS
import fintech as ft
import datetime as date
import json

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
	indexCode = request.args.get('index')
	print(indexCode)

	if not indexCode: print("No code")
	else:
		ICs, weights = ft.GetICsAndWeights(date.datetime(2017, 9, 15), indexCode)
		indices = list()
		for i in range(0,len(ICs)):
			thisIndex = {
				"value" : weights[i],
				"name" : ICs[i]
			}
			indices.append(thisIndex)
		return jsonify(indices)
	return jsonify("None")



if __name__ == '__main__':
	app.run()