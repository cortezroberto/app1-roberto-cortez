# Modulo y Clase
from flask import  Flask, render_template, url_for, redirect, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

# Creamos objeto tipo Flask y recibe de parametro nombre de aplicación
app = Flask(__name__)
app.debug = True # Debug permite ver cambios al momento
Bootstrap(app)


# Configuracion conexion postgress
# app.config['SQLAlCHEMY_DATABASE_URI']='postgresql+psycopg2://{user}:{password}@{direccion}:{puerto}/{basededaotos}'
# app.config['SQLALCHEMY_DATABASE_URI']='postgresql+psycopg2://postgres:12345@localhost:5432/dbprueba'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://lmnmmudnvsosvj:d637f8449b776ad68e2e1ca074b497839ff065260144b01762aa8e5e28a2390c@ec2-54-157-78-113.compute-1.amazonaws.com:5432/daamhnr9s6u8s9'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db = SQLAlchemy(app) #Objeto SQLAlchemy 

#modelo de datos
class Alumnos(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(30))
    apellido = db.Column(db.String(100))

lista = ["Acerca", "Nosotros", "Contacto", "Preguntas frecuentes"]

# Decorador, permite manejar una peticion
@app.route('/', methods=['GET','POST']) #endpoint
def index():
    print("index")
    if request.method == "POST":
        print("request")
        campo_nombre = request.form['nombre']
        campo_apellido = request.form['apellido']
        alumno = Alumnos(nombre = campo_nombre, apellido = campo_apellido)
        db.session.add(alumno)
        db.session.commit()
        mensaje = "Alumno registrado"
        # usuario = request.form['usuario']
        return render_template('index.html',mensaje = mensaje)
    return render_template("index.html", lista = lista) #asignacion
    #return redirect(url_for('acerca'))

@app.route('/acerca')
def acerca():
    consulta = Alumnos.query.all()
    print(consulta)
    return render_template("acerca.html",variable = consulta)


# Ejecutar de manera automatica el servidor a traves de Run()
if __name__ == "__main__":
    app.run() 
    