from flask import Flask, jsonify, request
import re

app = Flask(__name__)

# Creating dummy data for testing
users = [
    {'user_id': 1,'first_name': 'Isa', 'last_name': 'Faisal', 'email': 'IsaFaisal@gmail.com'},
    {'user_id': 2,'first_name': 'Chris', 'last_name': 'Hemsworth', 'email': 'Chrishemsworth@hotmail.com'}
]

# Create new user using POST
@app.route('/api/users', methods=['POST'])
def create_user():
    # Making variable "data" to store data for validation
    data = request.json
    # Data validation for required fields
    if 'first_name' not in data or not data['first_name']:
        return jsonify({'error': 'First name is required'})
    if 'last_name' not in data or not data['last_name']:
        return jsonify({'error': 'Last name is required'})
    if 'email' not in data or not data['email']:
        return jsonify({'error': 'Email is required'})
    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', data['email']):
        return jsonify({'error': 'Invalid email format'})

    new_user = {
        'user_id': len(users) + 1,
        'first_name': request.json['first_name'],
        'last_name': request.json['last_name'],
        'email': request.json['email']
    }

    users.append(new_user)
    return jsonify(new_user)

# Read all users using GET
@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Read a single user using GET
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user['user_id'] == user_id:
            return jsonify(user)

    return jsonify({'error': 'User not found'})

# Update specific user information using PUT
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    # Data validation for required fields
    if 'first_name' not in data or not data['first_name']:
        return jsonify({'error': 'First name is required'})
    if 'last_name' not in data or not data['last_name']:
        return jsonify({'error': 'Last name is required'})
    if 'email' not in data or not data['email']:
        return jsonify({'error': 'Email is required'})
    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', data['email']):
        return jsonify({'error': 'Invalid email format'})    

    for user in users:
        if user['user_id'] == user_id:            
            user['first_name'] = request.json['first_name']
            user['last_name'] = request.json['last_name']
            user['email'] = request.json['email']
            return jsonify(user)
    return jsonify({'error': 'User not found'})

# Delete a User using DELETE
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    for user in users:
        if user['user_id'] == user_id:
            users.remove(user)
            return jsonify({'data': f'user with user id {user_id} deleted successfully'})

    return jsonify({'error': 'User not found'})

if __name__ == '__main__':
    app.run(debug=True)
