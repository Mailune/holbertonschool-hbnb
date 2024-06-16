from flask_restx import Namespace, Resource, fields

# Define a namespace for place operations
places_ns = Namespace('places', description='Place operations')

# Define the place model for input/output validation
place_model = places_ns.model('Place', {
    'id': fields.String(required=True, description='Place ID'),
    'name': fields.String(required=True, description='Place name'),
    'description': fields.String(required=True, description='Description'),
})

# In-memory storage for places
places_db = {}

@places_ns.route('/')
class PlaceList(Resource):
    @places_ns.marshal_list_with(place_model)
    def get(self):
        '''Retrieve all places'''
        return list(places_db.values())

    @places_ns.expect(place_model)
    @places_ns.marshal_with(place_model, code=201)
    def post(self):
        '''Add a new place'''
        new_place = places_ns.payload
        new_place['id'] = str(len(places_db) + 1)  # Generate a new place ID
        places_db[new_place['id']] = new_place
        return new_place, 201

@places_ns.route('/<string:place_id>')
class PlaceResource(Resource):
    @places_ns.marshal_with(place_model)
    def get(self, place_id):
        '''Get place by ID'''
        place = places_db.get(place_id)
        if not place:
            places_ns.abort(404, "Place not found")
        return place

    @places_ns.expect(place_model)
    @places_ns.marshal_with(place_model)
    def put(self, place_id):
        '''Update place by ID'''
        if place_id not in places_db:
            places_ns.abort(404, "Place not found")
        place = places_ns.payload
        place['id'] = place_id
        places_db[place_id] = place
        return place

    def delete(self, place_id):
        '''Remove place by ID'''
        if place_id in places_db:
            del places_db[place_id]
            return '', 204
        places_ns.abort(404, "Place not found")
