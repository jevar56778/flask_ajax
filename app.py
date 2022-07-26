from flask import Flask,request,redirect,render_template,jsonify,url_for,make_response,session
import user
import animal


app = Flask(__name__,template_folder='plantillas')

app.config['SECRET_KEY']='holamundo'


@app.route('/')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/jum')
def jum():
    return render_template('jum.html')


@app.route('/hh')
def hh():
    cant = user.contar_usuario()
    return render_template('pdf.html',cant=cant)



#=====Ruta para los usuarios
@app.route('/listar_datos',methods=['GET'])
def listar_datos():
    if request.method == 'GET':
       usu=user.consultar_usuario()
       return jsonify(usu)

@app.route('/agregar_user',methods=['POST'])
def agregar_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        color = request.form['color']
        edad = request.form['edad']
        
        user.guardar_usuario(email,password,username,color,edad)
        
        return 'ok men'
    
@app.route('/eliminar_user',methods=['GET','POST'])
def eliminar_user():
    if request.method == 'POST':
        user.eliminar_usuario(request.form['id'])
    
    return 'Usuario Eliminado'

@app.route('/obtener_dato/<int:id>',methods=['GET','POST'])
def obtener_dato(id):
    if request.method == 'GET':
        
        retornar = user.obtener_usuario(id)
        
        return jsonify(retornar)


@app.route('/actualizar_dato',methods=['POST'])
def actualizar_dato():
    if request.method == 'POST':
        id = request.form['id']
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        color = request.form['color']
        edad = request.form['edad']
        
        user.actualizar_usuario(email,password,username,color,edad,id)
        
        return 'Datos Actualizados'
    
    
@app.route('/contar_dato',methods=['GET','POST'])
def contar_dato():
    if request.method == 'GET':
        cant=user.contar_usuario()
        
        print(cant)
        
    return jsonify(cant)


@app.route('/buscar',methods=['GET','POST'])
def buscar():
    if request.method == 'POST':
        
        buscar = request.form['buscar']
        bus =user.buscar_usuario(buscar)
        
    return jsonify(bus)

@app.route('/iniciar',methods=['POST','GET'])
def iniciar():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        init = user.iniciar(email,password)
        
        if init:
            session['logedin'] = True
            session['id'] = init['id']
            session['email'] = init['email']
            
            return redirect(url_for('index'))
        else:
            msg = 'El usuario o la contraseña son incorrectos'
            
            return msg
        
        
        

@app.route('/salir',methods=['POST','GET'])
def salir():
    session.pop('logedin',None)
    session.pop('id', None)
    session.pop('email', None)
    
    return redirect(url_for('login'))
        
        
        

        
#=====Ruta para los usuarios

@app.route('/agregar_animal',methods=['POST'])
def agregar_animal():
    if request.method =='POST':
        nombre = request.form['nombre']
        colorido = request.form['colorido']
        
        animal.guardar_animal(nombre,colorido)
        
        return 'bien parce'
    
    


if __name__ == "__main__":
    app.run(debug=True)

