from flask import Flask, request, jsonify
from .. import db as d
from .. import app
students = []

@app.route('/add', methods=['POST'])
def add_user():
    # try:
        # Get data from the form
        name = request.form.get('name')
        age = int(request.form.get('age'))  # Assuming age is an integer
        collection=d.db['user-exp-collection']
        # Insert data into MongoDB
        user_data = {'name': name, 'age': age}
        result = collection.insert_one(user_data)

        return jsonify({'message': 'User added successfully', 'inserted_id': str(result.inserted_id)})

    # except Exception as e:
    #     return jsonify({'error': str(e)}), 500