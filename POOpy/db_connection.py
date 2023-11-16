import mysql.connector

def connect(host, user, password, database):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="base1234",
        database="northwind"
    )
    return connection
