from flask_restx import Namespace, Resource, fields

# Define a namespace for city operations
cities_ns = Namespace('cities', description='City operations')

# Define the city model for input/output validation
city_model = cities_ns.model('City', {
    'id': fields.String(required=True, description='City ID'),
    'name': fields.String(required=True, description='City name'),
    'description': fields.String(required=True, description='Description'),
})

# In-memory storage for cities
cities_db = {}

@cities_ns.route('/')
class CityList(Resource):
    @cities_ns.marshal_list_with(city_model)
    def get(self):
        '''Retrieve all cities'''
        return list(cities_db.values())

    @cities_ns.expect(city_model)
    @cities_ns.marshal_with(city_model, code=201)
    def post(self):
        '''Add a new city'''
        new_city = cities_ns.payload
        # Generate a new city ID and assign it
        new_city['id'] = str(len(cities_db) + 1)
        cities_db[new_city['id']] = new_city
        return new_city, 201

@cities_ns.route('/<string:city_id>')
class CityResource(Resource):
    @cities_ns.marshal_with(city_model)
    def get(self, city_id):
        '''Get city by ID'''
        city = cities_db.get(city_id)
        if not city:
            cities_ns.abort(404, "City not found")
        return city

    @cities_ns.expect(city_model)
    @cities_ns.marshal_with(city_model)
    def put(self, city_id):
        '''Update city by ID'''
        if city_id not in cities_db:
            cities_ns.abort(404, "City not found")
        city = cities_ns.payload
        city['id'] = city_id
        cities_db[city_id] = city
        return city

    def delete(self, city_id):
        '''Remove city by ID'''
        if city_id in cities_db:
            del cities_db[city_id]
            return '', 204
        cities_ns.abort(404, "City not found")
