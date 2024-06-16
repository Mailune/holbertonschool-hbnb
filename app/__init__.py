import logging
from flask import Flask, jsonify
from flask_restx import Api
from app.api.api_users import user_ns
from app.api.api_places import places_ns
from app.api.api_reviews import reviews_ns
from app.api.api_amenities import amenities_ns
from app.api.api_cities import cities_ns
from app.api.api_countries import countries_ns

logging.basicConfig(level=logging.DEBUG)

def create_app():
    app = Flask(__name__)
    api = Api(app, version='1.0', title='HBnB API',
              description='A simple API for HBnB Evolution project')

    api.add_namespace(user_ns, path='/api/api_users')
    api.add_namespace(places_ns, path='/api/api_places')
    api.add_namespace(reviews_ns, path='/api/api_reviews')
    api.add_namespace(amenities_ns, path='/api/api_amenities')
    api.add_namespace(cities_ns, path='/api/api_cities')
    api.add_namespace(countries_ns, path='/api/api_countries')

    @app.route('/')
    def home():
        return jsonify(message="Welcome to the HBnB API")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5001)
