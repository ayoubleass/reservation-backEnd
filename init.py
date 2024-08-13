from models.category import Category
from models.amenity import Amenity
from models.country import Country
from models.city import City
from models.role import Role
from models import storage
import os
import requests


def initialize_categories():
        predefined_categories = ['Maison', 'Appartement', 'Hotel', 'Cabane']  # Add your predefined categories here
        for category_name in predefined_categories:
            category = storage.getSession().query(Category).filter_by(name=category_name).first()
            if not category:
                category = Category(name=category_name)
                storage.getSession().add(category)
        storage.getSession().commit()


def initialize_amenities():
    predefined_amenities = ['Wifi', 'Parking', 'Swimming Pool', 'Gym', 
                            'Animaux acceptés', 'Vue panoramique sur la ville', 
                            'Espace de travail dédié', 'Vue panoramique sur la ville',
                            'Vue sur le parc']  
    for amenity_name in predefined_amenities:
        amenity = storage.getSession().query(Amenity).filter_by(name=amenity_name).first()
        if not amenity:
            amenity = Amenity(name=amenity_name)
            storage.getSession().add(amenity)
    storage.getSession().commit()




def initialize_countries(offset=0):
    offset = 0;
    response = requests.get("https://api.first.org/data/v1/countries?offset={}".format(offset))
    if response.status_code == 200:
        r_body = response.json()
        data = r_body['data']
        if offset > r_body.get('total'):
            print("Done!")
            return
        for key, value in data.items():
            country = Country(id=key,name=value.get('country'),region =value.get('region')) 
            storage.new(country).save()
    return initialize_countries(offset + len(data))
    

def initialize_cities():
    country = storage.all("Country")
    for country in country.values():
        r = requests.post("https://countriesnow.space/api/v0.1/countries/cities",
                            {"country" : country.name})
        if r.status_code == 200:
            response_body = r.json()
            for city_name in response_body['data']:
                city  = City(name=city_name, country_id= country.id)
                storage.new(city).save()
    print("Done!")
    

def init_roles():
    roles_names = ["travler", "host", "Admin"]
    for role_name in roles_names:
        exists = storage.getSession().query(Role).filter(Role.name == role_name).first()
        if not exists:
            role = Role(name=role_name)
            storage.new(role).save()
    print("Done!")
    
def add_more_catgories():
    predefined_categories = [ "Iconiques", "Campagne", "Bord de mer", "Piscines", "Arctique", "Patrimoine", "Chambres", "Camping", "Montagnes", "Lacs", "Tendance", "Luxe", "Cabanes", "Wow!", "Plages", "Tropical", "Déserts", "Îles", "Châteaux", "Design", "Tiny houses", "Historique", "Vignobles", "Ski", "Fermes" ]
    for category_name in predefined_categories:
        category = storage.getSession().query(Category).filter_by(name=category_name).first()
        if not category:
            category = Category(name=category_name)
            storage.getSession().add(category)
    storage.getSession().commit()

#initialize_categories()
#initialize_amenities()
#initialize_countries()
# initialize_cities()
# init_roles()
add_more_catgories()
