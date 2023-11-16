from db_connection import connect

connection = connect("localhost", "root", "base1234", "northwind")

cursor = connection.cursor()

new_product = {
    "ProductID": 81,  
    "ProductName": "Ron",
    "SupplierID": 1,  
    "CategoryID": 2,  
    "Unit": "210 unidades",
    "Price": 309.99 
}
#james
insert_query = "INSERT INTO Products (ProductID, ProductName, SupplierID, CategoryID, Unit, Price) VALUES (%(ProductID)s, %(ProductName)s, %(SupplierID)s, %(CategoryID)s, %(Unit)s, %(Price)s)"

cursor.execute(insert_query, new_product)
connection.commit()

cursor.close()
connection.close()
