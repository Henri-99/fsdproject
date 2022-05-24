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
	'''Return a list called ICs that contains the constituents of the 
	respective indexCode in the same month and year as the inputted rDate.'''
	
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
	print(colName)

	colNo = 0
	for col in cursor.description:
		if (col[0] == colName):
			break
		colNo += 1 

	# Find alpha codes and append to ICs list
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

	
	return ICs, weights

# Function 2


# Function 3


# Testing program
if __name__ == "__main__":
	a, b = GetICsAndWeights(date.datetime(2017, 9, 15), "ALTI")
	print(a)
	print(b)
