import pyodbc


class NWProducts:

    def __init__(self):
        self.server = 'databases.spartaglobal.academy'
        self.database = 'Northwind'
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        self.connection_string = "DRIVER={ODBC Driver 17 for SQL Server};"
        self.connection_string += f"SERVER={self.server};"
        self.connection_string += f"DATABASE={self.database};"
        self.connection_string += f"UID={self.username};"
        self.connection_string += f"PWD={self.password}"
        self.northwind = pyodbc.connect(self.connection_string)
        self.cursor = self.northwind.cursor()

    def _sql_query(self, sql_query):
        return  self.cursor.execute(sql_query)

    def average_unit_price(self):
        records = self._sql_query("SELECT * FROM Products")
        avg_list = []
        for row in records:
            #print(float((row[5])))
            avg_list.append(row.UnitPrice)
        avg_unit_price = sum(avg_list)/len(avg_list)
        return avg_unit_price

# Test the class code
if __name__== "__main__":
    average = NWProducts()
    print(average.average_unit_price())

















# cursor.execute("SELECT @@version;")
# cursor.execute("SELECT customerID FROM customers")
# cursor.execute("SELECT * FROM customers WHERE country = 'germany'")
# # everything = cursor.fetchall()
# # everything = cursor.fetchall()
# # row = cursor.fetchone()
# # print(row)
# # print(everything)
#
# # for row in cursor:
# #     print(row[0])
#
# cursor.execute("SELECT * FROM Products;")
#
# for row in cursor:
#     print(row.UnitPrice)

