import sys
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
	quarter = request.args.get('q').split('Q')
	if not indexCode or not quarter: print("No code")
	else:
		ICs, weights = ft.GetICsAndWeights(date.datetime(int(quarter[0]), int(quarter[1])*3, 1), indexCode)
		#weights, ICs = zip(*sorted(zip(weights, ICs), reverse=True))
		indices = list()
		small = 0
		for i in range(0,len(ICs)):
			if weights[i] < 0.005:
				small += weights[i]
			else:
				thisIndex = {
					"value" : weights[i],
					"name" : ICs[i]
				}
				indices.append(thisIndex)
		if (small > 0):
			indices.append({
				"value" : small,
				"name" : "OTHER"
			})
		return jsonify(indices)
	return jsonify("None")

@app.route('/stat', methods = ['GET'])
def stat():
	index = request.args.get('index')
	mktIndex = request.args.get('market')
	stat = request.args.get('s')
	quarter = request.args.get('q').split('Q')
	#date
	if not index or not mktIndex or not stat: print("Missing input")
	else:
		ICs, weights = ft.GetICsAndWeights(date.datetime(int(quarter[0]), int(quarter[1])*3, 1), index)
		betas, specVols, mktVol = ft.GetBetasMktAndSpecVols(date.datetime(int(quarter[0]), int(quarter[1])*3, 1), ICs, mktIndex)
		pfBeta, sysCov, pfSysVol, specCov, pfSpecVol, totCov, pfVol, corrMat = ft.CalcStats(weights, betas, mktVol, specVols)
		print(stat)
		if (stat == 'beta'):
			return jsonify(betas.tolist())
		elif (stat == 'specVols'):
			return jsonify(specVols.tolist())
		elif (stat == 'pfBeta'):
			return jsonify(pfBeta.tolist())
		elif (stat == 'sysCov'):
			return jsonify(sysCov.tolist())
		elif (stat == 'pfSysVol'):
			return jsonify(pfSysVol.tolist())
		elif (stat == 'specCov'):
			return jsonify(specCov.tolist())
		elif (stat == 'pfSpecVol'):
			return jsonify(pfSpecVol.tolist())
		elif (stat == 'totCov'):
			return jsonify(totCov.tolist())
		elif (stat == 'pfVol'):
			return jsonify(pfVol.tolist())
		elif (stat == 'corrMat'):
			return jsonify(corrMat.tolist())
		
	return jsonify("None")

@app.route('/stock', methods=['GET'])
def stock():
	stock = request.args.get('s')
	if not stock: print("No code")
	else:
		try:
			return jsonify(ft.getTimeSeries(stock))
		except:
			return jsonify("None")		
	return jsonify("None")

if __name__ == '__main__':
	app.run()