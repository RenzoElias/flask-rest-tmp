from app import app
from utils.db import db
# Para poder usar el app del app.py

with app.app_context():
    db.create_all()
    # Para crear las tablas de los modelos de datos


# Si este proyecto se ejecuta como archivo principal
if __name__ == "__main__":
    # Para que los cambios se actualize automaticamente - debug=True
    app.run(debug=True) 