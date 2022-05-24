import pyodbc
import numpy as np
import pandas as pd

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=localhost\SQLEXPRESS;'
                      'Database=AIFMRM_ERS;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM tbl_BA_Beta_Output')

data = pd.DataFrame()

for i in cursor:
	print(i)
	wait = input()