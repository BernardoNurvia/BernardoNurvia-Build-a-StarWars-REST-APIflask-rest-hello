from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)  
    user_name = db.Column(db.String(50), nullable=False, unique=True)
    first_name= db.Column(db.String(50), nullable=False)
    last_name=db.Column(db.String(50), nullable=False)
    address =db.Column(db.String(150), nullable=False)
    characters_favorites_relationship =db.relationship('CharactersFavorites', back_populates='user_id_relationship')
    planets_favorites_relationship = db.relationship('PlanetsFavorites', back_populates='user_id_relationship')
    starships_favorites_relationship =db.relationship('StarshipsFavorites', back_populates='user_id_relationship')
    vehicles_favorites_relationship =db.relationship('VehiclesFavorites', back_populates='user_id_relationship')
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'is_active': self.is_active,
            'name': self.first_name,
            'last_name': self.last_name,
            'user_name': self.user_name,
            'address': self.address
            # do not serialize the password, its a security breach
        }

class CharactersFavorites(db.Model):
    __tablename__='characters_favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_id_relationship = db.relationship('User', back_populates='characters_favorites_relationship')
    character_favorite = db.Column(db.Integer, db.ForeignKey('characters.id'))
    character_favorite_relationship= db.relationship('Character', back_populates='id_relationship')

    
    def __repr__(self):
        return f'Characters Favorites'

    def serialize(self):
        return {
            'id': self.id,
            'name': self.character_favorite
            }

class PlanetsFavorites(db.Model):
    __tablename__ = 'planets_favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_id_relationship = db.relationship('User', back_populates='planets_favorites_relationship')
    planet_favorite = db.Column(db.Integer, db.ForeignKey('planet.id'))
    planet_favorite_relationship= db.relationship('Planet', back_populates='id_relationship')

    def __repr__(self):
        return f'Planets Favorites'

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'planet_id': self.user_id
          
        }
class StarshipsFavorites(db.Model):
    __tablename__ = 'starships_favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_id_relationship = db.relationship('User', back_populates='starships_favorites_relationship')
    starship_favorite= db.Column(db.Integer, db.ForeignKey('starship.id'))
    starship_favorite_relationship = db.relationship('Starship', back_populates='id_relationship')
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            'id': self.id,
          
        }
    
class Starship(db.Model):
    __tablename__ ='starship'
    id = db.Column(db.Integer, primary_key=True)
    id_relationship = db.relationship('StarshipsFavorites', back_populates='starship_favorite_relationship')
    uid = db.Column(db.Integer) 
    name = db.Column(db.String(50))
    model = db.Column(db.String(100))
    starship_class =db.Column(db.String(100))
    manufacturer = db.Column(db.String(100))
    cost_in_credits = db.Column(db.Integer)
    length = db.Column(db.Integer)
    crew = db.Column(db.String(100))
    passengers = db.Column(db.Integer)
    max_atmosphering_speed = db.Column(db.Integer)
    hyperdrive_rating =db.Column(db.Integer)
    mglt = db.Column(db.Integer) 
    cargo_capacity = db.Column(db.Integer)
    consumables = db.Column(db.String(50)) 
    #pilots = db.Column(db.Integer, db.ForeignKey('characters.id'))
    pilots_relationship = db.relationship('Character', back_populates='starship_pilot_relationship')
   
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            'id': self.id,
          
        }
class VehiclesFavorites(db.Model):
    __tablename__ = 'vehicles_favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user_id_relationship = db.relationship('User', back_populates='vehicles_favorites_relationship')
    vehicle_favorite = db.Column(db.Integer, db.ForeignKey('vehicle.id'))
    vehicle_favorite_relationship = db.relationship('Vehicle', back_populates='id_relationship')
    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            'id': self.id,
          
        }

class Vehicle(db.Model):
    __tablename__='vehicle'
    id = db.Column(db.Integer,primary_key=True)
    id_relationship= db.relationship('VehiclesFavorites', back_populates='vehicle_favorite_relationship')
    uid = db.Column(db.Integer)
    name =db.Column(db.String(50))
    model = db.Column(db.String(50))
    vehicle_class = db.Column(db.String(50))
    manufacturer = db.Column(db.String(100))
    cost_in_credits = db.Column(db.Integer)
    length = db.Column(db.Integer)
    crew = db.Column(db.Integer)
    passengers = db.Column(db.Integer)
    max_atmosphering_speed = db.Column(db.Integer)
    cargo_capacity = db.Column(db.Integer)
    consumables = db.Column(db.String(100))
    #pilots = db.Column(db.Integer, db.ForeignKey('characters.id'))
    pilots_relationship = db.relationship('Character', back_populates='vehicle_pilot_relationship')
    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            'id': self.id,
          
        }
class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    id_relationship= db.relationship('CharactersFavorites', back_populates='character_favorite_relationship')
    uid = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(114), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    eye_color = db.Column(db.String(20), nullable=False)
    hair_color = db.Column(db.String(30), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    mass = db.Column(db.Integer, nullable=False)
    skin_color = db.Column(db.String(20), nullable=False)
    homeworld = db.Column(db.Integer, db.ForeignKey('planet.id'))
    homeworld_relationship = db.relationship('Planet', back_populates='characters_relationship')
    species = db.Column(db.Integer, db.ForeignKey('species.id'))
    species_relationship = db.relationship('Species', back_populates='characters_relationship')
    starship_pilot = db.Column(db.Integer, db.ForeignKey('starship.id'))
    starship_pilot_relationship = db.relationship('Starship', back_populates='pilots_relationship')
    vehicle_pilot = db.Column(db.Integer, db.ForeignKey('vehicle.id'))
    vehicle_pilot_relationship = db.relationship('Vehicle', back_populates='pilots_relationship')
    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            'id': self.id,
          
        }
class Planet(db.Model):
    __tablename__ ='planet'
    id = db.Column(db.Integer, primary_key=True)
    id_relationship= db.relationship('PlanetsFavorites', back_populates='planet_favorite_relationship')
    uid = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(114), nullable=False)
    population = db.Column(db.String(30), nullable=False)
    rotation_period = db.Column(db.Integer, nullable=False)
    orbital_period = db.Column(db.Integer, nullable=False)
    gravity = db.Column(db.String(120), nullable=False)
    climate = db.Column(db.String(50), nullable=False)
    terrain = db.Column(db.String(50), nullable=False)
    surface_water = db.Column(db.Integer, nullable=False)
    species_relationship = db.relationship('Species', back_populates='planet_relationship')
    characters_relationship = db.relationship('Character', back_populates='homeworld_relationship')
    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            'id': self.id,
          
        }
class Species(db.Model):
    __tablename__ = 'species'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    classification = db.Column(db.String(100), nullable=False)
    designation = db.Column(db.String(100), nullable=False)
    average_height = db.Column(db.Integer)
    average_lifespan = db.Column(db.Integer)
    hair_colors = db.Column(db.String(50), nullable=False)
    skin_colors = db.Column(db.String(50), nullable=False)
    eye_colors = db.Column(db.String(50), nullable=False)
    planet = db.Column(db.Integer, db.ForeignKey('planet.id'))
    planet_relationship = db.relationship('Planet', back_populates='species_relationship')
    characters_relationship = db.relationship('Character', back_populates='species_relationship')
    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            'id': self.id,
          
        }
