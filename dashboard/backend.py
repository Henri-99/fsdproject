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
# rDate: one of the quarter end dates corresponding to reporting dates
# indexCode: "ALSI", "FLED", "LRGC", etc
#
def GetICsAndWeights(rDate, indexCode):
	'''return a string column vector/list called ICs that contains 
	the constituents of the respective indexCode in the same month and year 
	as the inputted rDate.'''
	
	query = 'SELECT * FROM tbl_Index_Constituents'
	cursor.execute(query)

	ICs = list()

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

		# Isolate records by year and month
		recordDate = record[0]
		if (rDate.year != recordDate.year or rDate.month != recordDate.month):
			continue

		# Isolate records by index column
		if (record[colNo] == indexCode):
			ICs.append(record[2])
			#print(record[0], record[2], record[colNo])

	return ICs

print(GetICsAndWeights(date.datetime(2017, 9, 15), "ALTI"))



# Function 2


# Function 3
