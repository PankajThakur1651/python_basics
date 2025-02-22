import mysql.connector
import connection_handler as ch

connection_handler = ch.ConnectionHandler()
conn, cursor = connection_handler.get_connection()

cursor.execute('select * from users')
row = cursor.fetchone()

while row is not None:
    print(row)
    row = cursor.fetchone()

connection_handler.close_connection()
