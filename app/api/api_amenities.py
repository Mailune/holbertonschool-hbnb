from flask_restx import Namespace, Resource, fields

# Namespace for amenity operations
amenities_ns = Namespace('amenities', description='Amenity operations')

# Amenity model for input/output validation
amenity_model = amenities_ns.model('Amenity', {
    'id': fields.String(required=True, description='Amenity ID'),
    'name': fields.String(required=True, description='Amenity name')
})

# In-memory storage for amenities
amenities_db = {}

@amenities_ns.route('/')
class AmenityList(Resource):
    @amenities_ns.marshal_list_with(amenity_model)
    def get(self):
        '''Retrieve all amenities'''
        return list(amenities_db.values())

    @amenities_ns.expect(amenity_model)
    @amenities_ns.marshal_with(amenity_model, code=201)
    def post(self):
        '''Add a new amenity'''
        new_amenity = amenities_ns.payload
        amenity_id = str(len(amenities_db) + 1)
        new_amenity['id'] = amenity_id
        amenities_db[amenity_id] = new_amenity
        return new_amenity, 201

@amenities_ns.route('/<string:amenity_id>')
class AmenityResource(Resource):
    @amenities_ns.marshal_with(amenity_model)
    def get(self, amenity_id):
        '''Fetch an amenity by ID'''
        amenity = amenities_db.get(amenity_id)
        if amenity is None:
            amenities_ns.abort(404, "Amenity not found")
        return amenity

    @amenities_ns.expect(amenity_model)
    @amenities_ns.marshal_with(amenity_model)
    def put(self, amenity_id):
        '''Update an amenity by ID'''
        if amenity_id not in amenities_db:
            amenities_ns.abort(404, "Amenity not found")
        updated_amenity = amenities_ns.payload
        updated_amenity['id'] = amenity_id
        amenities_db[amenity_id] = updated_amenity
        return updated_amenity

    def delete(self, amenity_id):
        '''Delete an amenity by ID'''
        if amenity_id in amenities_db:
            del amenities_db[amenity_id]
            return '', 204
        amenities_ns.abort(404, "Amenity not found")
