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
from models import db, Users, CharactersFavorites, PlanetsFavorites, StarshipsFavorites, Starship, VehiclesFavorites, Vehicle, Character, Planet, Species
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
#estas son los GET:
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

@app.route('/users/favorites', methods=['GET'])
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


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
