from flask import Flask, request, jsonify
from models import db, User, People, Planet, FavoritePeople, FavoritePlanet


#Variables iniciales para poder crear nuestro servidor y nuestra base de datos
app= Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/StarWars.db" #Aca definimos el nombre de la base de datos
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)





#2-Crear los endpoint
#People
@app.route('/people', methods=['GET']) #Definimos la primera ruta de la API GET/
def getPeople():
    all_people = People.query.all()
    all_people = list(map(lambda x: x.serialize(),all_people))
    return jsonify (all_people, "estas en people")

@app.route('/people/<int:id>',methods=['GET'] )
def getPeoplebyId(id):
    people = People.query.get(id)
    if not people:
        return jsonify({"error": "Person not found"}), 404
    return jsonify(people.serialize(), "Estas en peoplebyID")



#Planet
@app.route('/planet', methods=['GET'])  #Ruta para planeta
def getPlanet():
    all_planet = Planet.query.all()
    all_planet = list(map(lambda x: x.serialize(),all_planet))
    return jsonify (all_planet, "Estas en planeta!")

@app.route('/planet/<int:id>', methods = ['GET'])
def getPlanetById(id):
    planet = Planet.query.all(id)
    if not planet:
        return jsonify({"error": "Planet not found"}), 404
    return jsonify(planet.serialize(), "Estas en planetById")


#User 
@app.route('/user', methods =['GET'])
def getUser():
    all_user = User.query.all()
    all_user = list(map(lambda x: x.serialize(),all_user))
    return jsonify (all_user, "Estas en User!")

@app.route('/user/favorite', metods = ['GET'])
def getUserFavorites():
    #Usamos un usuario fijo (id=1)
    user_id = 1

    favorite_people = FavoritePeople.query.filter_by(user_id).all()
    favorite_planet = FavoritePlanet.query.filter_by(user_id).all()

    return jsonify({
        "favorite_people":[f.serialize() for f in favorite_people],
        "favorite_planet":[f.serialize() for f in favorite_planet],
    }),200





#FAVORITOS-----------------
@app.route('/favorites/people/<int:people_id>', methods = ['POST'])
def addFavoritePeople(people_id):
    












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
