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
Authentication
JWT Token Required for protected endpoints
Get Token: Use /login endpoint
Include Token: Authorization: Bearer <token>

🔐 Authentication Endpoints
Login
Authenticate user and get JWT token
Method: POST
URL: /login
Authentication: None
Request Body
json
{
  "email": "user@example.com",
  "password": "your_password"
}
Response
json
{
  "id": "user_id",
  "first_name": "John",
  "last_name": "Doe",
  "email": "user@example.com",
  "roles": ["traveler"],
  "token": "jwt_token_here"
}
cURL Example
bash
curl -X POST http://127.0.0.1:5000/api/v1/login \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "password123"}'

👥 Users Endpoints
Get All Users
Retrieves all users (Admin only)
Method: GET
URL: /users
Authentication: Required (JWT)
cURL Example
bash
curl -X GET http://127.0.0.1:5000/api/v1/users \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"

Get Specific User
Retrieves a specific user by ID
Method: GET
URL: /users/<user_id>
Authentication: None
cURL Example
bash
curl -X GET http://127.0.0.1:5000/api/v1/users/user_id_123

Create User
Register a new user
Method: POST
URL: /users
Authentication: None
Request Body
json
{
  "email": "newuser@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "password": "secure_password",
  "phone_number": "+1234567890",
  "role": "traveler"
}
cURL Example
bash
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
Update user information
Method: PUT
URL: /users/<user_id>
Authentication: Required (JWT)
cURL Example
bash
curl -X PUT http://127.0.0.1:5000/api/v1/users/user_id_123 \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"first_name": "Johnny", "phone_number": "+1987654321"}'

Delete User
Delete a user account
Method: DELETE
URL: /users/<user_id>
Authentication: Required (JWT)
cURL Example
bash
curl -X DELETE http://127.0.0.1:5000/api/v1/users/user_id_123 \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"

🏙️ Countries Endpoints
Get All Countries
Retrieves all countries
Method: GET
URL: /countries
Authentication: None
cURL Example
bash
curl -X GET http://127.0.0.1:5000/api/v1/countries

Get Specific Country
Retrieves a specific country by ID
Method: GET
URL: /countries/<country_id>
Authentication: None
cURL Example
bash
curl -X GET http://127.0.0.1:5000/api/v1/countries/FR

Create Country
Create a new country
Method: POST
URL: /countries
Authentication: None
cURL Example
bash
curl -X POST http://127.0.0.1:5000/api/v1/countries \
  -H "Content-Type: application/json" \
  -d '{"name": "France"}'

Update Country
Update country information
Method: PUT
URL: /countries/<country_id>
Authentication: None
cURL Example
bash
curl -X PUT http://127.0.0.1:5000/api/v1/countries/FR \
  -H "Content-Type: application/json" \
  -d '{"name": "French Republic"}'

Delete Country
Delete a country
Method: DELETE
URL: /countries/<country_id>
Authentication: None
cURL Example
bash
curl -X DELETE http://127.0.0.1:5000/api/v1/countries/FR

🏙️ Cities Endpoints
Get Cities by Country
Retrieves all cities in a country
Method: GET
URL: /country/<country_id>/cities
Authentication: None
cURL Example
bash
curl -X GET http://127.0.0.1:5000/api/v1/country/FR/cities

Get Specific City
Retrieves a specific city by ID
Method: GET
URL: /cities/<city_id>
Authentication: None
cURL Example
bash
curl -X GET http://127.0.0.1:5000/api/v1/cities/city_id_123

Create City
Create a new city in a country
Method: POST
URL: /country/<country_id>/cities
Authentication: None
cURL Example
bash
curl -X POST http://127.0.0.1:5000/api/v1/country/FR/cities \
  -H "Content-Type: application/json" \
  -d '{"name": "Paris"}'

🏠 Places Endpoints
Get Places by City
Retrieves all places in a city
Method: GET
URL: /cities/<city_id>/places
Authentication: None
Response
json
[
  {
    "id": "place_id",
    "name": "Beautiful Apartment",
    "description": "Luxury apartment in city center",
    "price_by_night": 120,
    "max_guest": 4,
    "images": [
      "http://127.0.0.1:5000/api/v1/images/photo1.jpg"
    ]
  }
]
cURL Example
bash
curl -X GET http://127.0.0.1:5000/api/v1/cities/city_id_123/places

Get Specific Place
Retrieves a specific place by ID
Method: GET
URL: /places/<place_id>
Authentication: None
cURL Example
bash
curl -X GET http://127.0.0.1:5000/api/v1/places/place_id_123

Get User's Places
Retrieves all places owned by a user
Method: GET
URL: /users/<user_id>/places
Authentication: None
cURL Example
bash
curl -X GET http://127.0.0.1:5000/api/v1/users/user_id_123/places

Create Place
Create a new place listing
Method: POST
URL: /cities/<city_id>/places
Authentication: Required (JWT)
Content-Type: multipart/form-data
Form Data
text
name: Beautiful Apartment
description: Luxury apartment
max_guest: 4
number_rooms: 2
number_bathrooms: 1
address: 123 Main St
price_by_night: 120
category_id: category_id
user_id: user_id
amenities[]: amenity_id1,amenity_id2
images: [file uploads]


🏠 Amenities Endpoints
Get All Amenities
Retrieves a list of all amenity objects
Method: GET
URL: /amenities
Authentication: None
Response
json
[
  {
    "id": "amenity_id_1",
    "name": "WiFi",
    "created_at": "2023-10-01T12:00:00.000000",
    "updated_at": "2023-10-01T12:00:00.000000"
  }
]
cURL Example
bash
curl -X GET http://127.0.0.1:5000/api/v1/amenities

Get Specific Amenity
Retrieves a specific amenity by ID
Method: GET
URL: /amenities/<amenity_id>
Authentication: None
cURL Example
bash
curl -X GET http://127.0.0.1:5000/api/v1/amenities/amenity_id_123

Create New Amenity
Creates a new amenity
Method: POST
URL: /amenities
Authentication: None
Headers: Content-Type: application/json
Request Body
json
{
  "name": "Swimming Pool"
}
cURL Example
bash
curl -X POST http://127.0.0.1:5000/api/v1/amenities \
  -H "Content-Type: application/json" \
  -d '{"name": "Swimming Pool"}'

Update Amenity
Updates an existing amenity
Method: PUT
URL: /amenities/<amenity_id>
Authentication: None
Headers: Content-Type: application/json
cURL Example
bash
curl -X PUT http://127.0.0.1:5000/api/v1/amenities/amenity_id_123 \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated Amenity Name"}'

Delete Amenity
Deletes a specific amenity
Method: DELETE
URL: /amenities/<amenity_id>
Authentication: None
cURL Example
bash
curl -X DELETE http://127.0.0.1:5000/api/v1/amenities/amenity_id_123

🏙️ Cities Endpoints
Get Cities by Country
Retrieves all cities in a specific country
Method: GET
URL: /country/<country_id>/cities
Authentication: None
cURL Example
bash
curl -X GET http://127.0.0.1:5000/api/v1/country/FR/cities

Get Specific City
Retrieves a specific city by ID
Method: GET
URL: /cities/<city_id>
Authentication: None
cURL Example
bash
curl -X GET http://127.0.0.1:5000/api/v1/cities/city_id_123

Create City
Creates a new city in a country
Method: POST
URL: /country/<country_id>/cities
Authentication: None
Headers: Content-Type: application/json
Request Body
json
{
  "name": "Paris"
}
cURL Example
bash
curl -X POST http://127.0.0.1:5000/api/v1/country/FR/cities \
  -H "Content-Type: application/json" \
  -d '{"name": "Paris"}'

Update City
Updates an existing city
Method: PUT
URL: /cities/<city_id>
Authentication: None
Headers: Content-Type: application/json
cURL Example
bash
curl -X PUT http://127.0.0.1:5000/api/v1/cities/city_id_123 \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated City Name"}'

Delete City
Deletes a specific city
Method: DELETE
URL: /cities/<city_id>
Authentication: None
cURL Example
bash
curl -X DELETE http://127.0.0.1:5000/api/v1/cities/city_id_123

📁 Categories Endpoints
Get All Categories
Retrieves a list of all categories
Method: GET
URL: /categories
Authentication: None
Response
json
[
  {
    "id": "category_id_1",
    "name": "Maison",
    "created_at": "2023-10-01T12:00:00.000000",
    "updated_at": "2023-10-01T12:00:00.000000"
  }
]
cURL Example
bash
curl -X GET http://127.0.0.1:5000/api/v1/categories

Get Specific Category
Retrieves a specific category by ID
Method: GET
URL: /categories/<category_id>
Authentication: None
cURL Example
bash
curl -X GET http://127.0.0.1:5000/api/v1/categories/category_id_123

Get Places by Category
Retrieves all places in a specific category
Method: GET
URL: /categories/<category_id>/places
Authentication: None
Response
json
[
  {
    "id": "place_id_1",
    "title": "Beautiful Apartment",
    "description": "Luxury apartment in city center",
    "price": 120,
    "images": [
      "http://127.0.0.1:5000/api/v1/images/image1.jpg",
      "http://127.0.0.1:5000/api/v1/images/image2.jpg"
    ]
  }
]
cURL Example
bash
curl -X GET http://127.0.0.1:5000/api/v1/categories/category_id_123/places

🖼️ Images Endpoint
Get Image
Retrieves an image by filename
Method: GET
URL: /images/<image_filename>
Authentication: None
cURL Example
bash
curl -X GET http://127.0.0.1:5000/api/v1/images/photo123.jpg

📋 Common Response Formats
Success Responses
200 OK - Successful request
201 Created - Resource successfully created
Error Responses
400 Bad Request - Invalid request format or missing required fields
404 Not Found - Resource not found
Error Response Format
json
{
  "error": "Error description"
}

🔧 Quick Testing Script
Create a test_api.sh file to test all endpoints:
bash
#!/bin/bash
BASE_URL="http://127.0.0.1:5000/api/v1"

echo "Testing Amenities Endpoints:"
curl -s "$BASE_URL/amenities" | jq . | head -10

echo -e "\nTesting Categories Endpoints:"
curl -s "$BASE_URL/categories" | jq . | head -10

echo -e "\nTesting Cities Endpoints:"
# Get first country ID to test cities
COUNTRY_ID=$(curl -s "$BASE_URL/countries" | jq -r '.[0].id')
curl -s "$BASE_URL/country/$COUNTRY_ID/cities" | jq . | head -10

📝 Usage Examples
Complete Workflow Example
Get all categories:
bash
curl -X GET http://127.0.0.1:5000/api/v1/categories
Get places in a category:
bash
curl -X GET http://127.0.0.1:5000/api/v1/categories/1/places
Create a new amenity:
bash
curl -X POST http://127.0.0.1:5000/api/v1/amenities \
  -H "Content-Type: application/json" \
  -d '{"name": "Air Conditioning"}'





