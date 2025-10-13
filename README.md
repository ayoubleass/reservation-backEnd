VacationRent - Airbnb-Style Reservation Platform
🏠 Overview
VacationRent is a comprehensive vacation rental platform that connects travelers with unique accommodations worldwide. From cozy apartments to luxury villas, our platform makes it easy to discover and book perfect stays for any trip.

VacationRent - Quick Setup Guide
🗄️ Database Setup (Already Done)
Since you have the SQL script ready, simply run:

# Create database
run:
bash
cat .sql | mysql -u root -p
update the file models/credentials.py with your MySQL credentials:

run:
bash
python init.py
After running the initialization, your database will have:

✅ Categories
Basic: Maison, Appartement, Hotel, Cabane

Extended: Iconiques, Campagne, Bord de mer, Piscines, Arctique, Patrimoine, Chambres, Camping, Montagnes, Lacs, Tendance, Luxe, Cabanes, Wow!, Plages, Tropical, Déserts, Îles, Châteaux, Design, Tiny houses, Historique, Vignobles, Ski, Fermes

✅ Amenities
Wifi, Parking, Swimming Pool, Gym

Animaux acceptés, Vue panoramique sur la ville

Espace de travail dédié, Vue sur le parc

✅ Countries & Cities
Real country data from API

Cities for each country

✅ User Roles
Traveler, Host, Admin

# VacationRent API Documentation
Base URL
text
http://127.0.0.1:5000/api/v1


    
Run app:
  python -m api.v1.app
