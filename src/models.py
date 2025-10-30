from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

# 1-Crear los modelos (tabla tradicional)

class User(db.Model):
    
    __tablename__ = "user" 

    # Ten en cuenta que cada columna es también un atributo normal de primera instancia de Python.
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique= True ,nullable=True)
    password= db.Column(db.String(120), nullable=False)
    is_active = db.Column(db.Boolean(), nullable=False)

    # El método serialize convierte el objeto en un diccionario
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email
            
        }

    

class People(db.Model):
    
    __tablename__ = "people" 

    # Ten en cuenta que cada columna es también un atributo normal de primera instancia de Python.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

    # El método serialize convierte el objeto en un diccionario
    def serialize(self):
        return {
            "id": self.id,
           
            "name": self.name
        }
    
class Planet(db.Model):
    
    __tablename__ = "planet" 

    # Ten en cuenta que cada columna es también un atributo normal de primera instancia de Python.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    climate= db.Column(db.String(120), nullable=False)

    # El método serialize convierte el objeto en un diccionario
    def serialize(self):
        return {
            "id": self.id,
            "climate": self.climate,
            "name": self.name
        }






 #TABLA DE FAVORITOS   
class FavoritePeople(db.Model):
    __tablename__ = "favoritesPeople" 

    id = db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer,  db.ForeignKey('user.id'))
    people_id =db.Column(db.Integer,  db.ForeignKey('people.id'))
    

    
    def serialize(self):
        return {
            "id": self.id,
            "user_id":self.user_id,
            "people_id": self.people_id
        }
    

class FavoritePlanet(db.Model):
    __tablename__ = "favoritesPlanet" 

    id = db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer,  db.ForeignKey('user.id'))
    planet_id =db.Column(db.Integer,  db.ForeignKey('planet.id'))
    

    
    def serialize(self):
        return {
            "id": self.id,
            "user_id":self.user_id,
            "planet_id": self.planet_id
        }






