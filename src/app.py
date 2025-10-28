from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


#Variables iniciales para poder crear nuestro servidor y nuestra base de datos
app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/StarWars.db" #Aca definimos el nombre de la base de datos
db = SQLAlchemy(app)


# 1-Crear los modelos (tabla tradicional)
class People(db.Model):
    # Aquí definimos el nombre de la tabla "Person"
    __tablename__ = "people" 

    # Ten en cuenta que cada columna es también un atributo normal de primera instancia de Python.
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False)

    # El método serialize convierte el objeto en un diccionario
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
        }
    
#2-Crear los endpoint
@app.route('/people') #Definimos la primera ruta de la API GET/
def getPeople():
    all_people = People.query.all()
    all_people = list(map(lambda x: x.serialize(),all_people))
    return jsonify (all_people, "estas en people")

@app.route('/people/<int:id>')
def getPeoplebyId(id):
    people = People.query.get(3)
    return jsonify (people, "Estas en peoplebyID")


#3 Iniciamos el servidor 
if __name__ == '__main__':

    with app.app_context():
        db.create_all()  #aqui crea la base de datos
    app.run(host = '0.0.0.0')