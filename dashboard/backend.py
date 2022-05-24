import pyodbc
import numpy as np
import pandas as pd

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

	return 0



cursor.execute('SELECT * FROM tbl_Index_Constituents')


# Function 2



# Function 3


data = pd.DataFrame()

for i in cursor:
	print(i)
	wait = input()