import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='vargas3627',
                    database='python',
                    auth_plugin='mysql_native_password'
                    )
