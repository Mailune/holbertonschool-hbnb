from flask_restx import Namespace, Resource, fields

# Define a namespace for country operations
countries_ns = Namespace('countries', description='Country operations')

# Define the country model for input/output validation
country_model = countries_ns.model('Country', {
    'id': fields.String(required=True, description='Country ID'),
    'name': fields.String(required=True, description='Country name'),
})

# In-memory storage for countries
countries_db = {}

@countries_ns.route('/')
class CountryList(Resource):
    @countries_ns.marshal_list_with(country_model)
    def get(self):
        '''Retrieve all countries'''
        return list(countries_db.values())

    @countries_ns.expect(country_model)
    @countries_ns.marshal_with(country_model, code=201)
    def post(self):
        '''Add a new country'''
        new_country = countries_ns.payload
        new_country['id'] = str(len(countries_db) + 1)  # Generate a new country ID
        countries_db[new_country['id']] = new_country
        return new_country, 201

@countries_ns.route('/<string:country_id>')
class CountryResource(Resource):
    @countries_ns.marshal_with(country_model)
    def get(self, country_id):
        '''Get country by ID'''
        country = countries_db.get(country_id)
        if not country:
            countries_ns.abort(404, "Country not found")
        return country

    @countries_ns.expect(country_model)
    @countries_ns.marshal_with(country_model)
    def put(self, country_id):
        '''Update country by ID'''
        if country_id not in countries_db:
            countries_ns.abort(404, "Country not found")
        country = countries_ns.payload
        country['id'] = country_id
        countries_db[country_id] = country
        return country

    def delete(self, country_id):
        '''Remove country by ID'''
        if country_id in countries_db:
            del countries_db[country_id]
            return '', 204
        countries_ns.abort(404, "Country not found")
