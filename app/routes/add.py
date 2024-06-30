from flask import Flask, request, jsonify
from datetime import datetime
from .. import db as d
from .. import app
students = []

@app.route('/add', methods=['POST'])
def add_user():
    try:
        if request.method == 'POST':
            id=request.form.get('ID')
            expDate=request.form.get('date')
            expAmount=float(request.form.get('amount'))
            expCategory=request.form.get('category')
            expName = request.form.get('name')
            collection=d.db['user-exp-collection']

            user_data = {
                            'ID': id,
                            'Expense Name': expName,
                            'Expense Category': expCategory,
                            'Expense Amount': expAmount,
                            'Expense Date': expDate,
                            'CreatedAt': datetime.now(),
                            'UpdatedAt': datetime.now()                    
                        }
            result = collection.insert_one(user_data)

            return jsonify({'message': 'User added successfully', 'inserted_id': str(result.inserted_id)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500