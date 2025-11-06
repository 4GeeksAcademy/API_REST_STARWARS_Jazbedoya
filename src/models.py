from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

# 1-Crear los modelos (tabla tradicional)


class User(db.Model):

    __tablename__ = "users"

    # Ten en cuenta que cada columna es también un atributo normal de primera instancia de Python.
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
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

    __tablename__ = "planets"

    # Ten en cuenta que cada columna es también un atributo normal de primera instancia de Python.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    climate = db.Column(db.String(120), nullable=False)

    # El método serialize convierte el objeto en un diccionario
    def serialize(self):
        return {
            "id": self.id,
            "climate": self.climate,
            "name": self.name
        }

 # TABLA DE FAVORITOS


class FavoritePeople(db.Model):
    __tablename__ = "favoritesPeople"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,  db.ForeignKey('users.id'))
    people_id = db.Column(db.Integer,  db.ForeignKey('people.id'))

    user = db.relationship('User', backref='favorites_people', lazy=True)
    people = db.relationship('People', backref='favorites_people', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_id": self.people_id
        }


class FavoritePlanet(db.Model):
    __tablename__ = "favoritesPlanets"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,  db.ForeignKey('users.id'))
    planet_id = db.Column(db.Integer,  db.ForeignKey('planets.id'))

    user = db.relationship('User', backref='favorites_planets', lazy=True)
    planet = db.relationship('Planet', backref='favorites_planets', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id
        }
