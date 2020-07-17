import pyodbc

server = 'databases.spartaglobal.academy'
database = 'Northwind'

username = 'SA'
password = 'Passw0rd2018'

connection_string = "DRIVER={ODBC Driver 17 for SQL Server};"
connection_string += f"SERVER={server};"
connection_string += f"DATABASE={database};"
connection_string += f"UID={username};"
connection_string += f"PWD={password}"

northwind = pyodbc.connect(connection_string)
cursor = northwind.cursor()

# cursor.execute("SELECT @@version;")
# cursor.execute("SELECT customerID FROM customers")
cursor.execute("SELECT TOP 2 * FROM customers WHERE country = 'germany'")
# everything = cursor.fetchall()
everything = cursor.fetchone()
# row = cursor.fetchone()
# print(row)
print(everything)
