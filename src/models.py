from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

# 1-Crear los modelos (tabla tradicional)
class People(db.Model):
    
    __tablename__ = "people" 

    # Ten en cuenta que cada columna es también un atributo normal de primera instancia de Python.
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(250), nullable=True)
    name = db.Column(db.String(120), nullable=False)

    # El método serialize convierte el objeto en un diccionario
    def serialize(self):
        return {
            "id": self.id,
            "user": self.user,
            "name": self.name
        }

    
class FavoritePeople(db.Model):
    __tablename__ = "favoritesPeople" 

    id_user = db.Column(db.Integer, primary_key=True)
    id_people = db.Column(db.Integer,  primary_key=True)
    

    
    def serialize(self):
        return {
            "id_user": self.id_user,
            "id_people": self.id_people,
        }
    


