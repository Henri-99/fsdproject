import pyodbc

def connect():
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=localhost\SQLEXPRESS;'
                        'Database=AIFMRM_ERS;'
                        'Trusted_Connection=yes;')

    return conn.cursor()

def close(cursor):
    cursor.close()