import mysql.connector
from db_conex import Connection

class Product:
    def __init__(self, product_name, supplier_id, category_id, unit, price):
        self.product_name = product_name
        self.supplier_id = supplier_id
        self.category_id = category_id
        self.unit = unit
        self.price = price

def inG_Product():
    product_name = input("Ingrese el nombre del producto: ")
    supplier_id = int(input("Ingrese el ID del Proveedor: "))
    category_id = int(input("Ingrese el ID de la categoría: "))
    unit = input("Ingrese las unidades del producto: ")
    price = float(input("Ingrese el precio del producto: "))

    return Product(product_name, supplier_id, category_id, unit, price)

def insertProduct(product, db_connection):
    connection = db_connection.connect()

    if connection.is_connected():
        cursor = connection.cursor()

        insert_query = """INSERT INTO Products (ProductName, SupplierID, CategoryID, Unit, Price) 
        VALUES (%s, %s, %s, %s, %s)"""

        product_data = (
            product.product_name,
            product.supplier_id,
            product.category_id,
            product.unit,
            product.price
        )

        try:
            cursor.execute(insert_query, product_data)
            connection.commit()
            print("Datos Guardados!!!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            db_connection.disconnect()

new_product = inG_Product()
db_connection_instance = Connection(host="localhost", user="roott", password="base1234", database="northwind")
insertProduct(new_product, db_connection_instance)
