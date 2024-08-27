from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    is_active = db.Column(db.Boolean(), nullable=False)  
    user_name = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(150), nullable=False)
    favorites = db.relationship('Favorites', back_populates='user')
    
    def __repr__(self):
        return '<Users %r>' % self.user_name

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'is_active': self.is_active,
            'name': self.first_name,
            'last_name': self.last_name,
            'user_name': self.user_name,
            'address': self.address,
            'favorites': [favorite.serialize() for favorite in self.favorites]
            # do not serialize the password, its a security breach
        }

class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('Users', back_populates='favorites')
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=True)
    starship_id = db.Column(db.Integer, db.ForeignKey('starship.id'), nullable=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), nullable=True)
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'), nullable=True)
    
    planet = db.relationship('Planet', primaryjoin="Favorites.planet_id == Planet.id")
    starship = db.relationship('Starship', primaryjoin="Favorites.starship_id == Starship.id")
    vehicle = db.relationship('Vehicle', primaryjoin="Favorites.vehicle_id == Vehicle.id")
    character = db.relationship('Character', primaryjoin="Favorites.character_id == Character.id", back_populates='favorites')
    
    def __repr__(self):
        return '<Favorites %r>' % self.id

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'planet': self.planet.serialize() if self.planet else None,
            'starship': self.starship.serialize() if self.starship else None,
            'vehicle': self.vehicle.serialize() if self.vehicle else None,
            'character': self.character.serialize() if self.character else None
        }

class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
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
    favorites = db.relationship('Favorites', back_populates='character')
    
    def __repr__(self):
        return '<Character %r>' % self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'eye_color': self.eye_color,
            'hair_color': self.hair_color,
            'skin_color': self.skin_color,
            'mass': self.mass,
            'species': self.species,
            'homeworld': self.homeworld,
            'starship_pilot': self.starship_pilot,
            'vehicle_pilot': self.vehicle_pilot 
        }

class Starship(db.Model):
    __tablename__ ='starship'
    id = db.Column(db.Integer, primary_key=True)
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
        return '<Starship %r>' % self.id

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'model': self.model,
            'clase': self.starship_class,
            'passengers': self.passengers,
            'hyperdrive_rating': self.hyperdrive_rating,
            'cargo_capacity': self.cargo_capacity,
            'cost_in_credits': self.cost_in_credits,
            'length': self.length,
            'manufacturer': self.manufacturer,
            'crew': self.crew,
            'max_atmosphering_speed': self.max_atmosphering_speed,
            'mglt': self.mglt,
            'consumables': self.consumables          
        }

class Vehicle(db.Model):
    __tablename__='vehicle'
    id = db.Column(db.Integer,primary_key=True)
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
        return '<Vehicle %r>' % self.id

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'model': self.model,
            'vehicle_class': self.vehicle_class,
            'manufacturer': self.manufacturer,
            'cost_in_credits': self.cost_in_credits,
            'length': self.length,
            'crew': self.crew,
            'passengers': self.passengers,            
            'max_atmosphering_speed': self.max_atmosphering_speed,
            'consumables': self.consumables,   
            'cargo_capacity': self.cargo_capacity           
        }

class Planet(db.Model):
    __tablename__ ='planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(114), unique=True, nullable=False)
    population = db.Column(db.String(30), nullable=True)
    rotation_period = db.Column(db.Integer, nullable=True)
    orbital_period = db.Column(db.Integer, nullable=True)
    gravity = db.Column(db.String(120), nullable=True)
    climate = db.Column(db.String(50), nullable=True)
    terrain = db.Column(db.String(50), nullable=True)
    surface_water = db.Column(db.Integer, nullable=True)
    species_relationship = db.relationship('Species', back_populates='planet_relationship')
    characters_relationship = db.relationship('Character', back_populates='homeworld_relationship')
    
    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'population': self.population,
            'rotation_period': self.rotation_period,
            'orbital_period': self.orbital_period,
            'gravity': self.gravity,
            'climate': self.climate,
            'terrain': self.terrain,
            'surface_water': self.surface_water,
            }
class Species(db.Model):
    __tablename__ = 'species'
    id = db.Column(db.Integer, primary_key=True)
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
        return '<Species %r>' % self.name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'classification': self.classification,
            'designation': self.designation,
            'average_height': self.average_height,
            'average_lifespan': self.average_lifespan,                 
        }
