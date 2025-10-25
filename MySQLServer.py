import mysql.connector
CREATE DATABASE IF NOT EXIST alx_book_store
db_connection = mysql.connector.connect(host="localhost",user="root",password="SQL.Pass.98")
print("Connection successful.")
