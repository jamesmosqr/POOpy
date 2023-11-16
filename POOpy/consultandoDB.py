from db_connection import connect
from tabulate import tabulate

connection = connect("localhost", "root", "base1234", "northwind")

with connection.cursor() as cursor:
    cursor.execute("SELECT ProductID, ProductName, SupplierID, CategoryID, Unit, Price FROM Products")

    data = cursor.fetchall()

    print(tabulate(data, headers=["ID PRODUCTO", "NOMBRE PRODUCTO", "SUPLIER ID", 
                                  "ID CATEGORIA", "UNIDADES", "PRECIO"], tablefmt="grid"))

connection.close()
