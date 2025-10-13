VacationRent - Airbnb-Style Reservation Platform
🏠 Overview
VacationRent is a comprehensive vacation rental platform that connects travelers with unique accommodations worldwide. From cozy apartments to luxury villas, our platform makes it easy to discover and book perfect stays for any trip.

VacationRent - Quick Setup Guide
🗄️ Database Setup (Already Done)
Since you have the SQL script ready, simply run:

bash
# Import the database schema
  cat your_database_file.sql | mysql -u root -p

run:
bash
python your_initialization_file.py


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

    
Run app:
  python -m api.v1.app
