import pyodbc
import numpy as np
import pandas as pd
import datetime as date

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=localhost\SQLEXPRESS;'
                      'Database=AIFMRM_ERS;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

# Function 1
def GetICsAndWeights(rDate, indexCode):
	'''Return 
	(1) a vector called ICs that contains the constituents of the 
	respective indexCode in the same month and year as the inputted rDate.
	(2) a vector called weights that contains the percentage contribution of
	each stock to the respective index'''
	
	query = 'SELECT * FROM tbl_Index_Constituents'
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

		# Skip records outside given date
		recordDate = record[0]
		if (rDate.year != recordDate.year or rDate.month != recordDate.month):
			continue

		# Isolate records by index column
		if (record[colNo] == indexCode):
			ICs.append(record[2])
			weights.append(record[10]) # Column 10 is gross market cap
			totalCap = totalCap + record[10]

	for i in range(0, len(weights)):
		weights[i] = round(weights[i]/totalCap,3)

	return np.array(ICs), np.array(weights)

# Function 2
def GetBetasMktAndSpecVols(rDate, ICs, mktIndexCode):
	'''
	return a numeric column vector/list called betas that contains the betas of the respective shares contained in ICs, in the same month and year as the inputted rDate

	mktIndexCode: "J203", "J200", "J250", "J257", "J258"
	'''
	query = 'SELECT * FROM tbl_BA_Beta_Output'
	cursor.execute(query)

	betas = list()
	specVols = list()
	totVols = list()
	mktVols = list()

	# Find relevent records
	for record in cursor:
		# Skip records outside given date
		recordDate = record[0]
		if (rDate.year != recordDate.year or rDate.month != recordDate.month):
			continue
		#print(record[0:2])
	
		instrument = record[1]
		if instrument in ICs:
			betas.append(record[8])   	# betas in column 8
			specVols.append(record[-1]) # specific vol. in last column
			totVols.append(record[-2])  # total vol. in second last column
		
	# Calculate market volatility from betas, total + specific volatilites
	for i in range(len(betas)):
		totRisk = totVols[i]
		uniRisk = specVols[i]
		beta = betas[i]
		if (totRisk != 0 and uniRisk != 0 and beta != 0):
			mktVol = np.sqrt(totRisk**2 - uniRisk**2)/beta
			#print(i,":",mktVol)
			mktVols.append(mktVol)
	mktVol = np.median(mktVols)

	return betas, specVols, mktVol

# Function 3



# Testing program
if __name__ == "__main__":
	a, b = GetICsAndWeights(date.datetime(2017, 9, 15), "ALTI")
	# print(a)
	# print(b)

	c, d, e = GetBetasMktAndSpecVols(date.datetime(2017, 9, 15), a, "J203")

	print("Market volatility:", e)