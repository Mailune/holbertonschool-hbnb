from flask_restx import Namespace, Resource, fields

# Define a namespace for review operations
reviews_ns = Namespace('reviews', description='Review operations')

# Define the review model for input/output validation
review_model = reviews_ns.model('Review', {
    'id': fields.String(required=True, description='Review ID'),
    'user_id': fields.String(required=True, description='User ID'),
    'place_id': fields.String(required=True, description='Place ID'),
    'rating': fields.Integer(required=True, description='Rating'),
    'text': fields.String(required=True, description='Review text'),
})

# In-memory storage for reviews
reviews_db = {}

@reviews_ns.route('/')
class ReviewList(Resource):
    @reviews_ns.marshal_list_with(review_model)
    def get(self):
        '''Retrieve all reviews'''
        return list(reviews_db.values())

    @reviews_ns.expect(review_model)
    @reviews_ns.marshal_with(review_model, code=201)
    def post(self):
        '''Add a new review'''
        new_review = reviews_ns.payload
        new_review['id'] = str(len(reviews_db) + 1)  # Generate a new review ID
        reviews_db[new_review['id']] = new_review
        return new_review, 201

@reviews_ns.route('/<string:review_id>')
class ReviewResource(Resource):
    @reviews_ns.marshal_with(review_model)
    def get(self, review_id):
        '''Get review by ID'''
        review = reviews_db.get(review_id)
        if not review:
            reviews_ns.abort(404, "Review not found")
        return review

    @reviews_ns.expect(review_model)
    @reviews_ns.marshal_with(review_model)
    def put(self, review_id):
        '''Update review by ID'''
        if review_id not in reviews_db:
            reviews_ns.abort(404, "Review not found")
        review = reviews_ns.payload
        review['id'] = review_id
        reviews_db[review_id] = review
        return review

    def delete(self, review_id):
        '''Remove review by ID'''
        if review_id in reviews_db:
            del reviews_db[review_id]
            return '', 204
        reviews_ns.abort(404, "Review not found")
