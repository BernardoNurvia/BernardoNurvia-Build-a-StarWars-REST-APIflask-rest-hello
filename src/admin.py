import os
from flask_admin import Admin
from models import db, Users, Favorites, CharactersFavorites, PlanetsFavorites, StarshipsFavorites, Starship, VehiclesFavorites, Vehicle, Character, Planet, Species 
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(Users, db.session))
    admin.add_view(ModelView(Favorites,db.session))
    admin.add_view(ModelView(Character, db.session))
    admin.add_view(ModelView(CharactersFavorites, db.session))
    admin.add_view(ModelView(Planet, db.session))
    admin.add_view(ModelView(PlanetsFavorites, db.session))
    admin.add_view(ModelView(Starship, db.session))
    admin.add_view(ModelView(StarshipsFavorites, db.session))
    admin.add_view(ModelView(Vehicle, db.session))
    admin.add_view(ModelView(VehiclesFavorites, db.session))
    admin.add_view(ModelView(Species, db.session))
  
    
   
   
    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))