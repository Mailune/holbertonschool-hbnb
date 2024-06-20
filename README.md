<p align="center"> 

<img width="830" alt="Bannière projet hbnb" src="https://github.com/Mailune/holbertonschool-hbnb/assets/156970898/eac98d43-d2be-4243-9a73-50415232a3a2">

## Description

#### 👋 Welcome to the HBNB README! 

This README serves as guide to understanding our HBNB.

HBNB is a specialized platform built to streamline the management of vacation rentals. Powered by a Python Flask backend API, it facilitates essential operations like user registration, property listing updates, booking management, and more.

So, let's dive in and explore our HBNB!

## OVERVIEW

HBNB is a comprehensive platform designed for efficiently managing vacation rentals. It features a robust backend API developed in Python using Flask, enabling seamless CRUD (Create, Read, Update, Delete) operations for users, property listings, and bookings. 

The HBnB Evolution project is crafted to guide you through the process of developing a web application from inception to deployment. You'll construct a comprehensive web application that includes:

- Architectural Design: Planning and structuring the application using Unified Modeling Language (UML).
- Testing and Validation: Developing comprehensive tests to validate the API and ensure the integrity of the business logic.
- API Implementation: Building the backend API using Flask, a versatile and powerful web framework.
- Data Storage Solutions: Implementing an initial file-based storage system to manage and store application data efficiently.
- Containerization with Docker: Packaging the application into Docker containers to facilitate easy deployment, scalability, and portability.

## Project Organization:

 - Interface Layer: This layer manages all incoming requests and formulates appropriate responses.
- Processing Layer: Here, the application processes and executes core operations, making critical decisions as needed.
- Storage Layer (persistence): Initially based on file storage, this layer oversees data management, ensuring secure and reliable storage.

## 🔹  UML Diagram of classes

<img width="830" alt="UML DIAGRAM" src="https://github.com/Mailune/holbertonschool-hbnb/assets/156970898/01a936f7-3f00-474f-94e3-de1aaffdf657">

## Installation & Running
```
Version : MacOs 14.4.1
```
```
Clone the repository:

git clone https://github.com/Mailune/holbertonschool-hbnb.git
```
```
Navigate to the project directory:

cd holbertonschool-hbnb
```
```
Create a virtual environment and activate it:

python3 -m venv venv
source venv/bin/activate
```
```
Docker image and start the containers with Docker Compose:

docker build -t mon_application_flask .

docker run -p 5001:5001 mon_application_flask

```
```
Open your browser and navigate to http://localhost:5001/ or http://127.0.0.1:5001 or to access the API graphical interface.
```

## CONFIGURATION: 
```
 Software/Framework        Version         Description 

 Flask                      2.0.2       Micro web framework for Python 
 Flask-RESTful                -         Extension for building REST APIs with Flask
Flask-SQLAlchemy              -         Flask extension for SQLAlchemy integration     |
pytest                      6.2.4       Framework for running Python tests
Flask-RESTx                 0.5.1       Extension for adding swagger to Flask APIs 
Gunicorn                    20.1.0      Python WSGI HTTP Server for Unix 
Werkzeug                    2.0.2       WSGI utility library for Python 
Docker                      26.1.3      Containerization platform 
Ubuntu                      22.04 LTS   Linux distribution 
```
## API ENDPOINTS

### User Management
- **Register**: `POST /api/api_users`
- **Login**: `POST /api/auth/login`
- **Profile**: `GET /api/api_users/<user_id>`

### Listing Management
- **Create Listing**: `POST /api/listings`
- **Update Listing**: `PUT /api/listings/<listing_id>`
- **Delete Listing**: `DELETE /api/listings/<listing_id>`
- **View Listings**: `GET /api/listings`

### Booking Management
- **Create Booking**: `POST /api/bookings`
- **Cancel Booking**: `DELETE /api/bookings/<booking_id>`
- **View Bookings**: `GET /api/bookings`


## TESTING :
 ```
   pip install -r requirements.txt
```
```
run the unit tests, use the following command:

python3 -m unittest discover -s tests -p "test_*.py" -v
```
```
Results:
----------------------------------------------------------------------
Ran 73 tests in 0.208s

OK
```
## FILES DESCRIPTION

  - **`app/`**: Contains the main application files.
  - `api/`: API endpoints for users, places, reviews, amenities, cities, and countries.
  - `models/`: Defines models for base model, user, place, review, amenity, city, and country.
  - `persistence/`: Handles database interactions and queries.
- **`tests/`**: Unit tests for API endpoints and models.
- **docker-compose.yml**: Docker Compose configuration file for container orchestration.
- **Dockerfile**: Dockerfile for building the Docker image of the application.
- **requirements.txt**: Lists all Python dependencies required by the application.
- **README.md**: Project documentation file containing an overview, API endpoints, installation instructions, and examples.
- **LICENSE**: Licensing information for the project.
- **data.json**: JSON data export from a database that contains information about reviews, users, and cities.
- **run.py**: to initialize and run a Flask web application.
- **AUTHORS**: to give the authors of the project.

## Authors:

#### 👤  Saïd Zaier
- Github: [@saidzaier10](https://github.com/saidzaier10)
- mail: said.zaier@holbertonstudents.com

#### 👤 Maïlys Rosereau
- Github: [@Mailune](https://github.com/Mailune)
- mail: 8831@holbertonstudents.com
 

Copyright (c) 2024 **Saïd Zaier & Maïlys Rosereau**
