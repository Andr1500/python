import pypyodbc  #pypyodbc is the module for DB


mySQLServer = "LOCALHOST/sqlservr"
myDatabase = "testDB"

connection = pypyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                'SERVER=' + mySQLServer + ';'
                                'DATABASE=' + myDatabase + ';')
#                                'UID=xxx;'
#                               'PWD=zzz;')


cursor = connection.cursor()

mySQLQuery = ("""
                SELECT * FROM Students
              """)

cursor.execute(mySQLQuery)
results = cursor.fetchall()
print(results)

connection.close()

#systemctl status mssql-server --no-pager   ODBC Driver 17 for SQL Server
