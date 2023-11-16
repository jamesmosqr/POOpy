from db_connection import connect
connection = connect("localhost", "root", "base1234", "northwind")
cursor = connection.cursor()


product_id_to_query = 80  # Reemplaza con el ProductID que deseas consultar

# Llama al procedimiento almacenado
cursor.callproc("GetProductByID", (product_id_to_query,))

# CREATE DEFINER=`root`@`localhost` PROCEDURE `northwind`.`GetProductByID`(IN product_id INT)
# BEGIN
# SELECT * FROM Products WHERE ProductID = product_id;  ojo este se debe ejecutar antes de crear la consulta
# END;

# CALL northwind.GetProductByID(1);

result = list(cursor.stored_results())[0]
product_data = result.fetchone()

cursor.close()
connection.close()

if product_data:
    print("PRODUCTO ID:", product_data[0])
    print("NOMBRE PRODUCTO:", product_data[1])
    print("PROVEEDOR ID:", product_data[2])
    print("CATEGORIA ID:", product_data[3])
    print("UNIDADES:", product_data[4])
    print("PRECIO: $", product_data[5])
else:
    print("Producto no encontrado")

# if product_data:
#     field_names = ["PRODUCTO ID", "NOMBRE PRODUCTO", "PROVEEDOR ID", "CATEGORIA ID", "UNIDADES", "PRECIO $"]
#     for field_name, field_value in zip(field_names, product_data):
#         print(f"{field_name}: {field_value}")
# else:
#     print("Producto no encontrado")
