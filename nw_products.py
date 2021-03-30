# class and object
import pyodbc


class NewProducts:
    def __init__(self):
        # Let's establish the connection using PYODBC
        server = "18.135.103.95"
        database = "Northwind"
        username = "SA"
        password = "Passw0rd2018"
        docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                          'SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

        cursor = docker_Northwind.cursor()
        # print(cursor.execute("SELECT @@version;"))
        # row = cursor.fetchone()

    def retrieve_data(self):
        # my_row = cursor.execute("CREATE TABLE Ula(id int IDENTITY(1,1) PRIMARY KEY,)")

        # row.commit()

        # my_row = cursor.execute("SELECT * FROM Ula").fetchall()
        # prod_row = cursor.execute("SELECT * FROM Products").fetchall()
        new_row = cursor.execute("SELECT * INTO UlaTable FROM Products")
        new_row = cursor.execute("SELECT * FROM UlaTable").fetchall()

        # print(prod_row)
        # print(my_row)
        print(new_row)
