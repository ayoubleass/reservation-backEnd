
from models import storage
import os


# def search_for_places():
#     #request_body = request.get_json()
#     country_id = 'BJ'
#     countries = storage.get("Country", country_id)
#     places = []
#     images_urls = []
#     for city in countries.cities:
#         for place in city.places:
#             image_urls = [" http://127.0.0.1:5000" +url_for('app_views.get_image', 
#                                                  image_filename=image.url.split('\\')[-1]) for image in place.images]
#             place_data =  place.to_dict()
#             #place_data['images'] = image_urls
#             places.append(place_data)
            
#     return countries.cities[0].places

# print("{}".format(search_for_places()))