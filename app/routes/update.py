from flask import Flask, request, jsonify, render_template_string
from datetime import datetime
from .. import db as d  
from .. import app  


@app.route('/update', methods=['POST'])
def update():
    try:
        collection = d.db['user-exp-collection']

        if request.method == 'POST':
            id = int(request.form.get('ID'))

            existing_expense = collection.find_one({'ID': id})

            if existing_expense:
                if request.form.get('date'):
                    existing_expense['Expense-date'] = request.form.get('date')
                if request.form.get('amount'):
                    existing_expense['Amount'] = float(request.form.get('amount'))
                if request.form.get('category'):
                    existing_expense['Expense-category'] = request.form.get('category')
                if request.form.get('name'):
                    existing_expense['Expense-name'] = request.form.get('name')

                existing_expense['UpdatedAt'] = datetime.now()

                collection.delete_one({'ID': id})

                result = collection.insert_one(existing_expense)

                return render_template_string('''
                    <script type="text/javascript">
                        alert('Expense updated successfully!');
                        window.location.href = "/";
                    </script>
                ''')

            else:
                return jsonify({'error': 'Expense not found with given ID'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500
