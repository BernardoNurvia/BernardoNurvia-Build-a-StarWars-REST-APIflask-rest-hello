"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Users, Favorites, Starship, Vehicle, Character, Planet, Species
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#Estas son los GET:
@app.route('/users', methods=['GET'])
def get_users():
    all_users = Users.query.all()
    all_users_serialize =[]
    for user in all_users:
        all_users_serialize.append(user.serialize())

    response_body = {
        "msg": "estos son lo usuarios",
        "data": all_users_serialize
    }

    return jsonify(response_body), 200

@app.route('/user/<int:id>', methods=['GET'])
def get_single_user(id):
    single_user = Users.query.get(id)
    if single_user is None:
        return jsonify({'Msg':f'El usuario con el id: {id} no existe'}), 404   
    response_body = {
        "msg": "estos son lo datos del usuario",
        "data": single_user.serialize()
    }
    return jsonify(response_body), 200

@app.route('/users/<int:user_id>/favorites', methods=['GET'])
def get_user_favorites(user_id):
    user = Users.query.get(user_id)
    if user is None:
        return jsonify({'Msg': f'El usuario con el id: {user_id} no existe'}), 404
    
    favorites = Favorites.query.filter_by(user_id=user_id).all()
    favorites_serialize = [favorite.serialize() for favorite in favorites]

    response_body = {
        "msg": "Estos son los favoritos del usuario",
        "data": favorites_serialize
    }

    return jsonify(response_body), 200

@app.route('/characters', methods=['GET'])
def get_characters():
    all_characters = Character.query.all()
    all_characters_serialize = []
    for character in all_characters:
        all_characters_serialize.append(character.serialize())

    response_body = {
        "msg": "Estos son los Personajes",
        "data": all_characters_serialize
    }

    return jsonify(response_body), 200

@app.route('/character/<int:id>', methods=['GET'])
def get_single_character(id):
    single_character = Character.query.get(id)
    if single_character is None:
        return jsonify({'Msg':f'El personaje con el id: {id} no existe'}), 404   
    response_body = {
        "msg": "estos son lo datos del personaje",
        "data": single_character.serialize()
    }
    return jsonify(response_body), 200

@app.route('/starships', methods=['GET'])
def get_starships():
    all_starships = Starship.query.all()
    all_starships_serialize = []
    for starship in all_starships:
        all_starships_serialize.append(starship.serialize())

    response_body = {
        "msg": "Estas son las Starships",
        "data": all_starships_serialize
    }

    return jsonify(response_body), 200

@app.route('/starship/<int:id>', methods=['GET'])
def get_single_starship(id):
    single_starship = Starship.query.get(id)
    if single_starship is None:
        return jsonify({'Msg':f'El starship con el id: {id} no existe'}), 404   
    response_body = {
        "msg": "estos son lo datos del planeta",
        "data": single_starship.serialize()
    }
    return jsonify(response_body), 200

@app.route('/vehicles', methods=['GET'])
def get_vehicles():
    all_vehicles = Vehicle.query.all()
    all_vehicles_serialize = []
    for vehicle in all_vehicles:
        all_vehicles_serialize.append(vehicle.serialize())

    response_body = {
        "msg": "Estos son los Vehicles",
        "data": all_vehicles_serialize
    }

    return jsonify(response_body), 200

@app.route('/vehicle/<int:id>', methods=['GET'])
def get_single_vehicle(id):
    single_vehicle = Vehicle.query.get(id)
    if single_vehicle is None:
        return jsonify({'Msg':f'El vehiculo con el id: {id} no existe'}), 404   
    response_body = {
        "msg": "estos son lo datos del planeta",
        "data": single_vehicle.serialize()
    }
    return jsonify(response_body), 200

@app.route('/planets', methods=['GET'])
def get_planets():
    all_planets = Planet.query.all()
    all_planets_serialize = []
    for planet in all_planets:
        all_planets_serialize.append(planet.serialize())

    response_body = {
        "msg": "Estos son los Planets",
        "data": all_planets_serialize
    }

    return jsonify(response_body), 200

@app.route('/planet/<int:id>', methods=['GET'])
def get_single_planets(id):
    single_planets = Planet.query.get(id)
    if single_planets is None:
        return jsonify({'Msg':f'El planeta con el id: {id} no existe'}), 404   
    response_body = {
        "msg": "estos son lo datos del planeta",
        "data": single_planets.serialize()
    }
    return jsonify(response_body), 200

@app.route('/species', methods=['GET'])
def get_species():
    all_species = Species.query.all()
    all_species_serialize = []
    for specie in all_species:
        all_species_serialize.append(specie.serialize())

    response_body = {
        "msg": "Estss son las species",
        "data": all_species_serialize
    }

    return jsonify(response_body), 200

#Estas son los POST:@app.route('/planet', methods=['POST'])
def add_planet():
    body = request.get_json(silent=True)
    if body is None:
        return jsonify({
            'msg': 'Debes enviar mínimo los datos requeridos de tu nuevo planeta',
            'Ejemplo': {
                'name': 'Campo requerido',
                'population': 'Campo requerido',
                'gravity': 'Campo requerido'
            }
        }), 400
    
    new_planet = Planet()
    new_planet.name = body.get('name')
    new_planet.population = body.get('population')
    new_planet.gravity = body.get('gravity')
    
    db.session.add(new_planet)
    db.session.commit()

    return jsonify({
        'msg': 'Tu planeta se ha creado correctamente, aunque faltan datos que podrás agregar posteriormente',
        'data': new_planet.serialize()
    }), 201

@app.route('/character', methods=['POST'])
def add_character():
    body = request.get_json(silent=True)
    if body is None:
        return jsonify({
            'Msg': 'Debes enviar al menos los siguientes campos',
            'Ejemplo': {
                'name': 'Campo requerido',
                'gender': 'Campo requerido',
                'eye_color': 'Campo requerido',
                'height': 'Campo requerido'
            }
        }), 400
    
    new_character = Character()
    new_character.name = body.get('name')
    new_character.gender = body.get('gender')
    new_character.eye_color = body.get('eye_color')
    new_character.height = body.get('height')
    
    db.session.add(new_character)
    db.session.commit()

    return jsonify({
        'Msg': 'Tu personaje se ha creado correctamente',
        'data': new_character.serialize()
    }), 201

@app.route('/favorites/planet/<int:planet_id>/<int:user_id>', methods=['POST'])
def add_favorite_planet(planet_id, user_id):
    user = Users.query.get(user_id)
    if user is None:
        return jsonify({'Msg': f'El usuario con el id: {user_id} no existe'}), 404
    
    planet = Planet.query.get(planet_id)
    if planet is None:
        return jsonify({'Msg': f'El planeta con el id: {planet_id} no existe'}), 404
    
    favorite = Favorites(user_id=user_id, planet_id=planet_id)
    db.session.add(favorite)
    db.session.commit()

    response_body = {
        "msg": "El planeta ha sido agregado a los favoritos del usuario",
        "data": favorite.serialize()
    }

    return jsonify(response_body), 200

@app.route('/favorite/people/<int:people_id>/', methods=['POST'])
def add_favorite_character(people_id):
    body = request.get_json(silent=True)
    user_id = body.get('user_id')
    
    user = Users.query.get(user_id)
    if user is None:
        return jsonify({'Msg': f'El usuario con el id: {user_id} no existe'}), 404
    
    character = Character.query.get(people_id)
    if character is None:
        return jsonify({'Msg': f'El personaje con el id: {people_id} no existe'}), 404
    
    favorite = Favorites(user_id=user_id, character_id=people_id)
    db.session.add(favorite)
    db.session.commit()

    response_body = {
        "msg": "El personaje ha sido agregado a los favoritos del usuario",
        "data": favorite.serialize()
    }

    return jsonify(response_body), 200
# aqui pongo los metodos DELETE

@app.route('/favorite/planet/<int:id_planet>', methods=['DELETE'])
def delete_favorite_planet(id_planet):
    body = request.get_json(silent=True)
    user_id = body.get('user_id')
    
    user = Users.query.get(user_id)
    if user is None:
        return jsonify({'Msg': f'El usuario con el id: {user_id} no existe'}), 404
    
    favorite = Favorites.query.filter_by(user_id=user_id, planet_id=id_planet).first()
    if favorite is None:
        return jsonify({'Msg': f'El planeta con el id: {id_planet} no está en los favoritos del usuario'}), 404
    
    db.session.delete(favorite)
    db.session.commit()

    response_body = {
        "msg": "El planeta ha sido eliminado de los favoritos del usuario"
    }

    return jsonify(response_body), 200

@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_favorite_character(people_id):
    body = request.get_json(silent=True)
    user_id = body.get('user_id')
    
    user = Users.query.get(user_id)
    if user is None:
        return jsonify({'Msg': f'El usuario con el id: {user_id} no existe'}), 404
    
    favorite = Favorites.query.filter_by(user_id=user_id, character_id=people_id).first()
    if favorite is None:
        return jsonify({'Msg': f'El personaje con el id: {people_id} no está en los favoritos del usuario'}), 404
    
    db.session.delete(favorite)
    db.session.commit()

    response_body = {
        "msg": "El personaje ha sido eliminado de los favoritos del usuario"
    }

    return jsonify(response_body), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
