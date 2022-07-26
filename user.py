from bd import obtener_conexion


def guardar_usuario(email,password,username,color,edad):
    conexion = obtener_conexion()
    cursor= conexion.cursor(dictionary=True)
    cursor.execute('insert into usuario(email,password,username,color,edad)values(%s,%s,%s,%s,%s)',
                   (email,password,username,color,edad))
    conexion.commit()
    conexion.close()
    


def consultar_usuario():
    usu = []
    conexion = obtener_conexion()
    cursor=conexion.cursor(dictionary=True)
    cursor.execute('select * from usuario')
    usu=cursor.fetchall()
    conexion.close()
    
    return usu


def eliminar_usuario(id):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("DELETE FROM usuario WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()
    

def obtener_usuario(id):
    conexion = obtener_conexion()
    retornar = None
    cursor = conexion.cursor(dictionary=True)
    cursor.execute('select email,password,username,color, edad from usuario where id = %s',(id,))
    retornar = cursor.fetchone()
    conexion.close()
    return retornar


def actualizar_usuario(email,password,username,color,edad,id):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute('update usuario set email = %s,password=%s,username= %s,color=%s,edad=%s where id=%s',
                   (email,password,username,color,edad,id))
    conexion.commit()
    conexion.close()
    
    
def contar_usuario():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute('select count(username) as cantidad from usuario')
    cant= cursor.fetchall()
    conexion.close()
    return cant

#controlador de busqueda
def buscar_usuario(buscar):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    sql = "select * from usuario where email LIKE '%"+buscar+"%' or username LIKE '%"+buscar+"%' or color LIKE '%"+buscar+"%'  or edad LIKE '%"+buscar+"%'"
    cursor.execute(sql)
    bus = cursor.fetchall()
    conexion.close()
    return bus


def iniciar(email,password):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute('select * from usuario where email = %s and password = %s',(email,password,))
    init = cursor.fetchone()
    conexion.close()
    return init