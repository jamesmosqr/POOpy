from db_connection import connect

connection = connect("localhost", "root", "base1234", "northwind")

cursor = connection.cursor()


product_id_to_delete = 81  # Reemplaza con el ProductID del producto que deseas eliminar

delete_query = "DELETE FROM Products WHERE ProductID = %s"

cursor.execute(delete_query, (product_id_to_delete,))

connection.commit()

cursor.close()
connection.close()
