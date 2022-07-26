from bd import obtener_conexion

def guardar_animal(nombre,colorido):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute('insert into animal(nombre,colorido)values(%s,%s)',
                   (nombre,colorido))
    conexion.commit()
    conexion.close
    