import mysql.connector
from tabulate import tabulate

def main():
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'base1234',
        database = "northwind"
    )

 

    with connection.cursor() as cursor:
        cursor.execute("select   CustomerID, CustomerName, ContactName, Address FROM customers")

        data = cursor.fetchall()

    print(tabulate(data, headers=["CustomerID", "NOMBRE DEL PRODUCTO", "SUPLIER ID", "ID CATEGORIA", "UNIDADES", "PRECIO"], tablefmt="pipe"))

    connection.close()
if __name__ == "__main__":
    main()