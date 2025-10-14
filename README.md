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

Run app:
  python -m api.v1.app

# VacationRent API Documentation
Base URL
text
http://127.0.0.1:5000/api/v1

## 🔐 Authentication

### JWT Token
Protected endpoints require a **JWT token**.  
- **Get Token:** via `/login`  
- **Include Token:**  
Authorization: Bearer <token>

---

## 🔑 Authentication Endpoints

### **Login**
Authenticate a user and receive a JWT token.

**Method:** `POST`  
**URL:** `/login`  
**Authentication:** None

#### 📨 Request Body
```json
{
"email": "user@example.com",
"password": "your_password"
}
📤 Response
json
Copier le code
{
  "id": "user_id",
  "first_name": "John",
  "last_name": "Doe",
  "email": "user@example.com",
  "roles": ["traveler"],
  "token": "jwt_token_here"
}
💻 cURL Example
bash
Copier le code
curl -X POST http://127.0.0.1:5000/api/v1/login \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "password123"}'
👥 Users Endpoints
Get All Users
Retrieve all users (Admin only).

Method: GET
URL: /users
Authentication: Required (JWT)

bash
Copier le code
curl -X GET http://127.0.0.1:5000/api/v1/users \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
Get Specific User
Retrieve a user by ID.
Method: GET
URL: /users/<user_id>
Authentication: None

bash
Copier le code
curl -X GET http://127.0.0.1:5000/api/v1/users/user_id_123
Create User
Register a new user.
Method: POST
URL: /users
Authentication: None

📨 Request Body
json
Copier le code
{
  "email": "newuser@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "password": "secure_password",
  "phone_number": "+1234567890",
  "role": "traveler"
}
bash
Copier le code
curl -X POST http://127.0.0.1:5000/api/v1/users \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "password": "password123",
    "phone_number": "+1234567890",
    "role": "traveler"
  }'
Update User
Update user information.
Method: PUT
URL: /users/<user_id>
Authentication: Required (JWT)

bash
Copier le code
curl -X PUT http://127.0.0.1:5000/api/v1/users/user_id_123 \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"first_name": "Johnny", "phone_number": "+1987654321"}'
Delete User
Delete a user account.
Method: DELETE
URL: /users/<user_id>
Authentication: Required (JWT)

bash
Copier le code
curl -X DELETE http://127.0.0.1:5000/api/v1/users/user_id_123 \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
🏙️ Countries Endpoints
Get All Countries
Method: GET
URL: /countries
Authentication: None

bash
Copier le code
curl -X GET http://127.0.0.1:5000/api/v1/countries
Get Specific Country
Method: GET
URL: /countries/<country_id>
Authentication: None

bash
Copier le code
curl -X GET http://127.0.0.1:5000/api/v1/countries/FR
Create Country
Method: POST
URL: /countries
Authentication: None

bash
Copier le code
curl -X POST http://127.0.0.1:5000/api/v1/countries \
  -H "Content-Type: application/json" \
  -d '{"name": "France"}'
Update Country
Method: PUT
URL: /countries/<country_id>
Authentication: None

bash
Copier le code
curl -X PUT http://127.0.0.1:5000/api/v1/countries/FR \
  -H "Content-Type: application/json" \
  -d '{"name": "French Republic"}'
Delete Country
Method: DELETE
URL: /countries/<country_id>
Authentication: None

bash
Copier le code
curl -X DELETE http://127.0.0.1:5000/api/v1/countries/FR
🌆 Cities Endpoints
Get Cities by Country
Method: GET
URL: /country/<country_id>/cities

bash
Copier le code
curl -X GET http://127.0.0.1:5000/api/v1/country/FR/cities
Get Specific City
Method: GET
URL: /cities/<city_id>

bash
Copier le code
curl -X GET http://127.0.0.1:5000/api/v1/cities/city_id_123
Create City
Method: POST
URL: /country/<country_id>/cities

bash
Copier le code
curl -X POST http://127.0.0.1:5000/api/v1/country/FR/cities \
  -H "Content-Type: application/json" \
  -d '{"name": "Paris"}'
🏠 Places Endpoints
Get Places by City
Method: GET
URL: /cities/<city_id>/places

bash
Copier le code
curl -X GET http://127.0.0.1:5000/api/v1/cities/city_id_123/places
Get Specific Place
Method: GET
URL: /places/<place_id>

bash
Copier le code
curl -X GET http://127.0.0.1:5000/api/v1/places/place_id_123
Create Place
Method: POST
URL: /cities/<city_id>/places
Authentication: Required (JWT)
Content-Type: multipart/form-data

bash
Copier le code
curl -X POST http://127.0.0.1:5000/api/v1/cities/city_id_123/places \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -F "name=Beautiful Apartment" \
  -F "description=Luxury apartment in city center" \
  -F "max_guest=4" \
  -F "number_rooms=2" \
  -F "number_bathrooms=1" \
  -F "address=123 Main Street" \
  -F "price_by_night=120" \
  -F "category_id=cat_123" \
  -F "user_id=user_123" \
  -F "amenities[]=amenity_1,amenity_2" \
  -F "images=@photo1.jpg"
Search Places
Method: POST
URL: /places_search

bash
Copier le code
curl -X POST http://127.0.0.1:5000/api/v1/places_search \
  -H "Content-Type: application/json" \
  -d '{
    "country_id": "FR",
    "arrival": "2024-01-15",
    "departure": "2024-01-20",
    "amenities": ["wifi", "parking"],
    "price_by_night": 150
  }'
🏠 Amenities Endpoints
Get All Amenities
Method: GET
URL: /amenities

bash
Copier le code
curl -X GET http://127.0.0.1:5000/api/v1/amenities
Create Amenity
Method: POST
URL: /amenities

bash
Copier le code
curl -X POST http://127.0.0.1:5000/api/v1/amenities \
  -H "Content-Type: application/json" \
  -d '{"name": "Swimming Pool"}'
🗂️ Categories Endpoints
Get All Categories
Method: GET
URL: /categories

bash
Copier le code
curl -X GET http://127.0.0.1:5000/api/v1/categories
Get Places by Category
Method: GET
URL: /categories/<category_id>/places

bash
Copier le code
curl -X GET http://127.0.0.1:5000/api/v1/categories/category_id_123/places
🖼️ Images Endpoint
Get Image
Method: GET
URL: /images/<image_filename>

bash
Copier le code
curl -X GET http://127.0.0.1:5000/api/v1/images/photo123.jpg
📋 Common Response Codes
Code	Meaning
200	✅ OK – Successful request
201	✨ Created – Resource created successfully
400	⚠️ Bad Request – Invalid input
401	🔒 Unauthorized – Authentication required
404	❌ Not Found – Resource not found

🔧 Quick Testing Script
You can quickly test all endpoints using this bash script:

bash
Copier le code
#!/bin/bash
BASE_URL="http://127.0.0.1:5000/api/v1"

echo "Testing Amenities:"
curl -s "$BASE_URL/amenities" | jq . | head -10

echo -e "\nTesting Categories:"
curl -s "$BASE_URL/categories" | jq . | head -10

echo -e "\nTesting Cities:"
COUNTRY_ID=$(curl -s "$BASE_URL/countries" | jq -r '.[0].id')
curl -s "$BASE_URL/country/$COUNTRY_ID/cities" | jq . | head -10
🧩 Usage Example
Complete workflow:

bash
Copier le code
# Get all categories
curl -X GET http://127.0.0.1:5000/api/v1/categories

# Get places in a category
curl -X GET http://127.0.0.1:5000/api/v1/categories/1/places

# Create a new amenity
curl -X POST http://127.0.0.1:5000/api/v1/amenities \
  -H "Content-Type: application/json" \
  -d '{"name": "Air Conditioning"}'
🧠 Notes
JWT tokens must be included in protected endpoints.

Ensure that your API server is running on http://127.0.0.1:5000/api/v1.

Use tools like Postman, Insomnia, or cURL to test the endpoints.
