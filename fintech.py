import database as db
import numpy as np
import pandas as pd
import datetime as date

# Function 1
def GetICsAndWeights(rDate, indexCode):
	'''Return 
	(1) a vector called ICs that contains the constituents of the 
	respective indexCode in the same month and year as the inputted rDate.
	(2) a vector called weights that contains the percentage contribution of
	each stock to the respective index'''
	
	query = 'SELECT * FROM tbl_Index_Constituents'
	cursor = db.connect()
	cursor.execute(query)

	ICs = list()
	weights = list()
	totalCap = 0

	# Find relevant column number from indexCode
	if (indexCode == "ALSI" or indexCode == "FLED"):
		colName = "ALSI New"
	elif (indexCode == "LRGC" or indexCode == "MIDC" or  indexCode == "SMLC"):
		colName = "Index New"
	else:
		colName = indexCode + " New"

	colNo = 0
	for col in cursor.description:
		if (col[0] == colName):
			break
		colNo += 1 

	# Find relevent records
	for record in cursor:

		# Skip records outside given year/month
		recordDate = record[0]
		if (rDate.year != recordDate.year or rDate.month != recordDate.month):
			continue

		# Isolate records by index column
		if (record[colNo] == indexCode):
			ICs.append(record[2])
			weights.append(record[10]) # Column 10 is gross market cap
			totalCap = totalCap + record[10]

	db.close(cursor)

	for i in range(0, len(weights)):
		weights[i] = weights[i]/totalCap

	return np.array(ICs), np.array(weights)

# Function 2
def GetBetasMktAndSpecVols(rDate, ICs, mktIndexCode):
	'''
	return a numeric column vector/list called betas that contains the betas of the respective shares contained in ICs, in the same month and year as the inputted rDate

	mktIndexCode: "J203", "J200", "J250", "J257", "J258"
	'''
	query = 'SELECT * FROM tbl_BA_Beta_Output'
	cursor = db.connect()
	cursor.execute(query)

	betas = list()
	specVols = list()
	totVols = list()

	# Find relevent records
	for record in cursor:
		recordDate = record[0]
		instrument = record[1]
		index = record[2]	
		
		# Skip records outside given date
		if (rDate.year != recordDate.year or rDate.month != recordDate.month):
			continue

		if (instrument in ICs and index == mktIndexCode):
			betas.append(record[8])   	# betas in column 8
			specVols.append(record[-1]) # specific vol. in last column
			totVols.append(record[-2])  # total vol. in second last column
		
		# Total market volatility
		if(instrument == index and index == mktIndexCode):
			mktVol = record[-2]
	db.close(cursor)

	# For 1-data-point shares, set beta=1 and vol=mktVol
	for i in range(0,len(betas)):
		if not betas[i]:
			betas[i] = 1
			specVols[i] = mktVol
			if not totVols[i]:
				totVols[i] = mktVol
		
	return np.array(betas), np.array(specVols), mktVol

# Function 3
def CalcStats(weights, betas, mktVol, specVols):
	weights = weights[:, np.newaxis]
	betas = betas[:, np.newaxis]
	specVols = specVols[:, np.newaxis]

	# Portfolio Beta
	pfBeta = np.matmul(weights.transpose(), betas)

	# Systematic Covariance Matrix
	sysCov = np.matmul(betas, betas.transpose()) * mktVol**2

	# Portfolio Systematic Variance
	pfSysVol = pfBeta * np.matmul(betas.transpose(), weights) * mktVol**2

	# Specific Covariance Matrix 
	specCov = np.matmul(np.diag(specVols.flat), np.diag(specVols.flat))

	# Portfolio Specific Variance
	pfSpecVol = np.matmul(np.matmul(weights.transpose(), specCov),weights)

	# Total Covariance Matrix
	totCov = sysCov + specCov

	# Portfolio Variance
	pfVol = pfSysVol + pfSpecVol

	# Correlation Matrix
	D = np.diagflat(np.diag(totCov))
	invD = np.linalg.inv(D) 
	corrMat = np.matmul(invD, np.matmul(totCov, invD))

	# Rounding for display purposes
	pfBeta = np.around(pfBeta, 5) 
	sysCov = np.around(sysCov, 5)
	pfSysVol = np.around(pfSysVol, 5)
	specCov = np.around(specCov, 5)
	pfSpecVol = np.around(pfSpecVol, 5)
	totCov = np.around(totCov, 5)
	pfVol = np.around(pfVol, 5)
	corrMat = np.around(corrMat, 5)


	return pfBeta, sysCov, pfSysVol, specCov, pfSpecVol, totCov, pfVol, corrMat

# Time Series
# Returns historic stock price data
def getTimeSeries(instrument):
	query = "SELECT * FROM tbl_EOD_Equity_Data WHERE [Instrument] = '" + instrument + "'"
	cursor = db.connect()
	cursor.execute(query)
	data = []
	for record in cursor:
		thisDate = [record[0].year, record[0].month, record[0].day]
		data.append({
			'name' : record[0].isoformat(),
			'value' : ['/'.join(str(x) for x in thisDate), record[2]]
		})
	db.close(cursor)
	return(data)

# Portfolio Builder
# Returns prices, totals, and weights given list of stocks and quantities
def GetPricesAndWeights(stocks, quantities):
	prices = []
	for i in range(len(stocks)):
		stocks[i] = stocks[i].upper()
		prices.append(0)

	totals = []
	weights = []
	data = []

	cap = 0
	query = "SELECT [Instrument], [Price] FROM tbl_EOD_Equity_Data WHERE [Date] = '2021-03-31'"
	cursor = db.connect()
	cursor.execute(query)
	for record in cursor:
		if record[0] in stocks:
			prices[stocks.index(record[0])] = int(record[1])
	db.close(cursor)

	if len(prices) == 0:
		return "None"

	for i in range(len(stocks)):
		total = int(quantities[i])*prices[i]
		totals.append(total)
		cap += total
		
	for i in range(len(stocks)):
		weights.append(round(float(totals[i])/float(cap),4))
		data.append({
			'price' : prices[i],
			'total' : totals[i],
			'weight' : weights[i]
		})


	return data

# Returns portfolio statistics and matrices
def customPfStats(stocks, weights, mktIndex):
	weights = np.array(weights)[:, np.newaxis]

	betas, specVols, mktVol = GetBetasMktAndSpecVols(date.datetime(2021, 3, 1), stocks, mktIndex)
	betas = betas[:, np.newaxis]
	specVols = specVols[:, np.newaxis]


	# Portfolio Beta
	pfBeta = np.matmul(weights.transpose(), betas)

	# Systematic Covariance Matrix
	sysCov = np.matmul(betas, betas.transpose()) * mktVol**2

	# Portfolio Systematic Variance
	pfSysVol = pfBeta * np.matmul(betas.transpose(), weights) * mktVol**2

	# Specific Covariance Matrix 
	specCov = np.matmul(np.diag(specVols.flat), np.diag(specVols.flat))

	# Portfolio Specific Variance
	pfSpecVol = np.matmul(np.matmul(weights.transpose(), specCov),weights)

	# Total Covariance Matrix
	totCov = sysCov + specCov

	# Portfolio Variance
	pfVol = pfSysVol + pfSpecVol

	# Correlation Matrix
	D = np.diagflat(np.diag(totCov))
	invD = np.linalg.inv(D) 
	corrMat = np.matmul(invD, np.matmul(totCov, invD))

	# Rounding for display purposes
	pfBeta = np.around(pfBeta, 5) 
	sysCov = np.around(sysCov, 5)
	pfSysVol = np.around(pfSysVol, 5)
	specCov = np.around(specCov, 5)
	pfSpecVol = np.around(pfSpecVol, 5)
	totCov = np.around(totCov, 5)
	pfVol = np.around(pfVol, 5)
	corrMat = np.around(corrMat, 5)


	return pfBeta, sysCov, pfSysVol, specCov, pfSpecVol, totCov, pfVol, corrMat

# Generates a list of tickers and company names for all equities in database
def GetEquitiesList():
	query = "SELECT [Alpha], [Instrument], [Gross Market Capitalisation] FROM tbl_Index_Constituents WHERE [Date] = '2021-03-23'" # ORDER BY [Gross Market Capitalisation] DESC"
	cursor = db.connect()
	cursor.execute(query)
	list = []
	for record in cursor:
		list.append(record[0] + " : " + record[1])
	# print(list)
	db.close(cursor)

# Testing program
if __name__ == "__main__":
	print("FinTech Module for FSD Project")
