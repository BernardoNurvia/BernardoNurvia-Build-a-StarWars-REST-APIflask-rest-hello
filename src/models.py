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

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active
            # do not serialize the password, its a security breach
        }

class CharactersFavorites(db.Model):
    __tablename__='characters_favorites'
    id = db.Colum(db.Interger, primary_key=True)
    user_id = db.Colum(db.Interger, db.ForeignKey('user.id'))
    user_id_relationship = db.relationship('User', back_populates='characters_favorites_relationship')
    character_favorite = db.Colum(db.Interger, db.ForeignKey('characters.id'))
    character_favorite_relationship= db.relationship('Character', back_populates='id_relationship')

    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
          
        }

class PlanetsFavorites(db.Model):
    __tablename__ = 'planets_favorites'
    id = db.Colum(db.Interger, primary_key=True)
    user_id = db.Colum(db.Interger, db.ForeignKey('user.id'))
    user_id_relationship = db.relationship('User', back_populates='planets_favorites_relationship')
    planet_favorite = db.Colum(db.Interger, db.ForeignKey('planets_favorites.id'))
    planet_favorite_relationship= db.relationship('Planet', back_populates='id_relationship')

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
          
        }
class StarshipsFavorites(db.Model):
    __tablename__ = 'starships_favorites'
    id = db.Colum(db.Interger, primary_key=True)
    user_id = db.Colum(db.Interger, db.ForeignKey('user.id'))
    user_id_relationship = db.relationship('User', back_populates='starships_favorites_relationship')
    starship_favorite= db.Colum(db.Interger, db.ForeignKey('starship.id'))
    starship_favorite_relationship = db.relationship('Starship', back_populates='id_relationship')
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
          
        }
    
class Starship(db.Model):
    __tablename__ ='starship'
    id = db.Colum(db.Interger, db.ForeignKey('starships_favorites.id'), primary_key=True)
    id_relationship = db.relationship('StarshipsFavorites', back_populates='starship_favorite_relationship')
    uid = db.Colum(db.Interger) 
    name = db.Colum(db.String(50))
    model = db.Colum(db.String(100))
    starship_class =db.Colum(db.String(100))
    manufacturer = db.Colum(db.String(100))
    cost_in_credits = db.Colum(db.Interger)
    length = db.Colum(db.Interger)
    crew = db.Colum(db.String(100))
    passengers = db.Colum(db.Interger)
    max_atmosphering_speed = db.Colum(db.Interger)
    hyperdrive_rating =db.Colum(db.Interger)
    mglt = db.Colum(db.Interger) 
    cargo_capacity = db.Colum(db.Interger)
    consumables = db.Colum(db.String(50)) 
    pilots = db.Colum(db.Interger, db.ForeignKey('characters.id'))
    pilots_relationship = db.relationship('Character', back_populates='starship_pilot_relationship')
   
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
          
        }
class VehiclesFavorites(db.Model):
    __tablename__ = 'vehicles_favorites'
    id = db.Colum(db.Interger, primary_key=True)
    user_id = db.Colum(db.Interger, db.ForeignKey('user.id'))
    user_id_relationship = db.relationship('User', back_populates='vehicles_favorites_relationship')
    vehicle_favorite = db.Colum(db.Interger, db.ForeignKey('vehicle.id'))
    vehicle_favorite_relationship = db.relationship('Vehicle', back_populates='id_relationship')
    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
          
        }

class Vehicle(db.Model):
    __tablename__='vehicle'
    id = db.Colum(db.Interger, db.ForeignKey('vehicles_favorites.id'), primary_key=True)
    id_relationship= db.relationship('VehiclesFavorites', back_populates='vehicle_favorite_relationship')
    uid = db.Colum(db.Interger)
    name =db.Colum(db.String(50))
    model = db.Colum(db.String(50))
    vehicle_class = db.Colum(db.String(50))
    manufacturer = db.Colum(db.String(100))
    cost_in_credits = db.Colum(db.Interger)
    length = db.Colum(db.Interger)
    crew = db.Colum(db.Interger)
    passengers = db.Colum(db.Interger)
    max_atmosphering_speed = db.Colum(db.Interger)
    cargo_capacity = db.Colum(db.Interger)
    consumables = db.Colum(db.String(100))
    pilots = db.Colum(db.Interger, db.ForeignKey('characters.id'))
    pilots_relationship = db.relationship('Character', back_populates='vehicle_pilot_relationship')
    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
          
        }
class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Colum(db.Interger, db.ForeignKey('characters_favorites.character_favorite'), primary_key=True)
    id_relationship= db.relationship('CharactersFavorites', back_populates='character_favorite_relationship')
    uid = db.Colum(db.Interger, nullable=False)
    name = db.Colum(db.String(114), nullable=False)
    gender = db.Colum(db.String(20), nullable=False)
    eye_color = db.Colum(db.String(20), nullable=False)
    hair_color = db.Colum(db.String(30), nullable=False)
    height = db.Colum(db.Interger, nullable=False)
    mass = db.Colum(db.Interger, nullable=False)
    skin_color = db.Colum(db.String(20), nullable=False)
    homeworld = db.Colum(db.Interger, db.ForeignKey('planets.id'))
    homeworld_relationship= db.relationship('Planet', back_populates='characters_relationship')
    species = db.Colum(db.Interger, db.ForeignKey('species.id'))
    species_relationship = db.relationship('Species', back_populates='characters_relationship')
    starship_pilot = db.Colum(db.Interger, db.ForeignKey('starship.id'))
    starship_pilot_relationship = db.relationship('Starship', back_populates='pilots_relationship')
    vehicle_pilot = db.Colum(db.Interger, db.ForeignKey('vehicle.id'))
    vehicle_pilot_relationship = db.relationship('Vehicle', back_populates='pilots_relationship')
    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
          
        }
class Planet(db.Model):
    __tablename__ ='planet'
    id = db.Colum(db.Integer, db.ForeignKey('planets_favorites.id'), primary_key=True)
    id_relationship= db.relationship('PlanetsFavorites', back_populates='planet_favorite_relationship')
    uid = db.Colum(db.Integer, nullable=False)
    name = db.Colum(db.String(114), nullable=False)
    population = db.Colum(db.String(30), nullable=False)
    rotation_period = db.Colum(db.Integer, nullable=False)
    orbital_period = db.Colum(db.Integer, nullable=False)
    gravity = db.Colum(db.String(120), nullable=False)
    climate = db.Colum(db.String(50), nullable=False)
    terrain = db.Colum(db.String(50), nullable=False)
    surface_water = db.Colum(db.Integer, nullable=False)
    species_relationship = db.relationship('Species', back_populates='planet_relationship')
    characters_relationship = db.relationship('Character', back_populates=' homeworld_relationship')
    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
          
        }
class Species(db.Model):
    __tablename__ = 'species'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    properties = db.Column(db.Integer, db.ForeignKey('species_properties.id'))
    properties_relationship = db.relationship('SpeciesProperty', back_populates='species_relationship')
    planet = db.Column(db.Integer, db.ForeignKey('planets.id'))
    planet_relationship = db.relationship('Planet', back_populates='species_relationship')
    characters_relationship = db.relationship('Character', back_populates='species_relationship')
    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
          
        }
class SpeciesProperty(db.Model):
    __tablename__ = 'species_properties'
    id = db.Column(db.Integer, primary_key=True)
    classification = db.Column(db.String(100), nullable=False)
    designation = db.Column(db.String(100), nullable=False)
    average_height = db.Column(db.Integer)
    average_lifespan = db.Column(db.Integer)
    hair_colors = db.Column(db.String(50), nullable=False)
    skin_colors = db.Column(db.String(50), nullable=False)
    eye_colors = db.Column(db.String(50), nullable=False)
    homeworld = db.Column(db.Integer, db.ForeignKey('planets.id'))
    homeworld_relationship = db.relationship('Planet', back_populates='species_relationship')
    species_relationship = db.relationship('Species', back_populates='properties_relationship')
    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
          
        }