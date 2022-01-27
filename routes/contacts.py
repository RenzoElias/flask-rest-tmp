# Para no estar importando cada archivo, entre uno y otro al estar seccionando el codigo para que sea escalable, en este caso separar el app con las rutas
# Se usara la clase o funcionalidad Blueprint de Flask, para poder dividir nuestra app en multiples partes , para crear una seccion dentro de la aplicacion
# render_templ - este modulo o funcion, es para poder renderizar o procesar el archivo html para devolverlo al navegador
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contact import Contact
from utils.db import db
# from app import app

# Esta seccion de la app, se nombrara Blueprint('contacts'
# Y se pone la propiedad __name__
# Blueprint('contacts', __name__) - Esto devuelve un enrutador que sera la variable contacts
# Es mas descriptivo esa variable ya que se sabe que esta relacionada a los contactos
contacts = Blueprint('contacts', __name__)

@contacts.route('/')
def index():
    # Trae todos los datos de la tabla
    # select * from contact;
    contacts = Contact.query.all()
    # Luego se le pasa por parametro a la variable contacts de color naranja
    
    # return "<h1>contacts list</h1>"
    # Se ejecuta el modulo, y no es necesario poner la direccion completa, solo con el nombre del archivo se podra, ya que el modulo por defecto extrae desde esa ruta templates
    return render_template('index.html', contacts=contacts)

@contacts.route('/new', methods=['POST'])
def add_contact():
    # print(request.form['fullname'])
    # print(request.form['email'])
    # print(request.form['phone'])
    
    fullname = request.form['fullname']
    email = request.form['email']
    phone = request.form['phone']
    
    # Definir un nuevo objeto, con el constructor
    new_contact = Contact(fullname, email, phone)
    
    print(new_contact)
    
    # Para guardar a la BD, lo que llenaste en el objeto nuevo Contact, es un model donde se guardo los datos entrantes
    db.session.add(new_contact)
    # Para guardar los cambios y acabar la conexion con la BD
    db.session.commit()
    
    flash("Contact added sucessfully!")
    
    # Redirecciona ahora ya no a una ruta, osea entra al metodo esta caso index
    return redirect(url_for('contacts.index'))
    # return redirect('/')
    # return "saving a contact"

@contacts.route('/update/<id>', methods=['POST', 'GET'])
def update(id):
    contact = Contact.query.get(id)
    if request.method == 'POST':
        contact.fullname = request.form['fullname']
        contact.email = request.form['email']
        contact.phone = request.form['phone']
        db.session.commit()
        
        flash("Contact updated sucessfully!")
        return redirect(url_for('contacts.index'))
        
    # else:
    return render_template('update.html', contact=contact)
    
    # contact = Contact.query.get(id)
    # print(id)
    # return render_template('update.html', contact=contact)
    # return "update a contact"

# @contacts.route('/delete')
# def delete_contact():
#     return "delete a contact"

@contacts.route('/delete/<id>')
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    flash("Contact deleted sucessfully!")
    # print(contact)
    return redirect(url_for('contacts.index'))
    # return redirect('/')
    # return "delete a contact"
    
@contacts.route('/about')
def about():
    return render_template("about.html")
 
# SQLAlchemy, Es un ORM que permite conectarse a la BD y hacer consulta, y todo con codigo de python, en lugar de usar codigo SQL