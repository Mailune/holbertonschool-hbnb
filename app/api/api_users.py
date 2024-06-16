from flask_restx import Namespace, Resource, fields

# Define a namespace for user operations
user_ns = Namespace('users', description='User operations')

# Define the user model for input/output validation
user_model = user_ns.model('User', {
    'id': fields.String(required=True, description='User ID'),
    'email': fields.String(required=True, description='User email'),
    'first_name': fields.String(required=True, description='First name'),
    'last_name': fields.String(required=True, description='Last name'),
})

# In-memory storage for users
users_db = {}

@user_ns.route('/')
class UserList(Resource):
    @user_ns.marshal_list_with(user_model)
    def get(self):
        '''Retrieve all users'''
        return list(users_db.values())

    @user_ns.expect(user_model)
    @user_ns.marshal_with(user_model, code=201)
    def post(self):
        '''Add a new user'''
        new_user = user_ns.payload
        new_user['id'] = str(len(users_db) + 1)  # Generate a new user ID
        users_db[new_user['id']] = new_user
        return new_user, 201

@user_ns.route('/<string:user_id>')
class UserResource(Resource):
    @user_ns.marshal_with(user_model)
    def get(self, user_id):
        '''Get user by ID'''
        user = users_db.get(user_id)
        if not user:
            user_ns.abort(404, "User not found")
        return user

    @user_ns.expect(user_model)
    @user_ns.marshal_with(user_model)
    def put(self, user_id):
        '''Update user by ID'''
        if user_id not in users_db:
            user_ns.abort(404, "User not found")
        user = user_ns.payload
        user['id'] = user_id
        users_db[user_id] = user
        return user

    def delete(self, user_id):
        '''Remove user by ID'''
        if user_id in users_db:
            del users_db[user_id]
            return '', 204
        user_ns.abort(404, "User not found")
