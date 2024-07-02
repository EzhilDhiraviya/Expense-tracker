from flask import Flask, request, jsonify, render_template_string
from datetime import datetime
from .. import db as d
from .. import app

students = []

@app.route('/add', methods=['POST'])
def addExpense():
    try:
        if request.method == 'POST':
            id = request.form.get('ID')
            expDate = request.form.get('date')
            expAmount = float(request.form.get('amount'))
            expCategory = request.form.get('category')
            expName = request.form.get('name')
            collection = d.db['user-exp-collection']

            user_data = {
                'ID': id,
                'Expense-name': expName,
                'Expense-category': expCategory,
                'Amount': expAmount,
                'Expense-date': expDate,
                'CreatedAt': datetime.now(),
                'UpdatedAt': datetime.now()
            }
            result = collection.insert_one(user_data)

            return render_template_string('''
                <script type="text/javascript">
                    alert('Expense added successfully!');
                    window.location.href = "/";
                </script>
            ''')
    except Exception as e:
        return jsonify({'error': str(e)}), 500
