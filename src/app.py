from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


#Variables iniciales para poder crear nuestro servidor y nuestra base de datos
app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/StarWars.db" #Aca definimos el nombre de la base de datos
db = SQLAlchemy(app)


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
    





#2-Crear los endpoint
@app.route('/people') #Definimos la primera ruta de la API GET/
def getPeople():
    all_people = People.query.all()
    all_people = list(map(lambda x: x.serialize(),all_people))
    return jsonify (all_people, "estas en people")

@app.route('/people/<int:id>')
def getPeoplebyId(id):
    people = People.query.get(id)
    if not people:
        return jsonify({"error": "Person not found"}), 404
    return jsonify(people.serialize(), "Estas en peoplebyID")


@app.route('/user/<int:user_id>/favorite/people/<int:people_id>', methods=["POST"])
def addPeoplebyId(user_id, people_id):
    favorite = FavoritePeople(id_user=user_id, id_people=people_id)
    db.session.add(favorite)
    db.session.commit()
    return("Se agrego correctamente el personaje")


#3 Iniciamos el servidor 
if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # Solo insertar si no hay datos todavía
        if not People.query.first():
            people1 = People(name="Luke Skywalker")
            people2 = People(name="Darth Vader")
            db.session.add_all([people1, people2])
            db.session.commit()

    # Ahora sí se ejecuta el servidor
    app.run(host='0.0.0.0', port=5000, debug=True)
