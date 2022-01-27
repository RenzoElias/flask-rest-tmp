from flask import Flask
from routes.contacts import contacts
from flask_sqlalchemy import SQLAlchemy
# Para utilizar la seccion blueprint contacts

# Ejecutar Flask y guardar en app
app = Flask(__name__)

app.secret_key = "secret key"
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:123456@localhost/contactsdb'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Se le pasa la configuracion de app, a SQLAchemy
SQLAlchemy(app)

# Ya que el blueprint sirve para definir una seccion
# Tambien ahora para poder importar o añadirlo a la app se hara asi
app.register_blueprint(contacts)

# Carpetas
# routes - Contendra las url apis
# models - Para poder modelar los datos, osea definir los datos que vamos a estar guardadndo dentro de la base de datos # Datos que queremos guardar en la base de datos
# templates - Para poder tener plantillas o vistas html es decir vamos a poder crear archivos html y poder enviales al navegador, para que se muestre una interfaz al usuario
# utils - Para poder tener la conexion a la base de datos, se usara el sqlalchemy
# index.py - Es el que va arrancar la app
# app.py - Va tener la configuracion de la aplicacion


# Ahora este archivo solo contiene el codigo de la app y configuracion, de la BD, de las sessiones, Secret Keys
# Las rutas estan por aparte y mucho mejor