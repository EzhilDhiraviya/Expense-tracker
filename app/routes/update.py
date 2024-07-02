from flask import Flask, request, jsonify , render_template_string
from datetime import datetime
from .. import db as d
from .. import app
students = []

@app.route('/update', methods=['POST'])
def update():
    try:
        collection = d.db['user-exp-collection']
        expName = None    
        expCategory = None  
        expAmount = None
        expDate = None
        created = None
        if request.method == 'POST':   

            id = int(request.form.get('ID'))
            cursor=collection.find({'ID':id})
            for doc in cursor:
                expName = doc['Expense-name']     
                expCategory = doc['Expense-category']  
                expAmount = doc['Amount']
                expDate = doc['Expense-date']
                created = doc['CreatedAt']

            if request.form.get('date') not in [None, ""]:
                expDate = request.form.get('date')
            if request.form.get('amount') not in [None, ""]:    
                expAmount = float(request.form.get('amount'))
            if request.form.get('category') not in [None, ""]:
                expCategory = request.form.get('category')
            if request.form.get('name') not in [None, ""]:
                expName = request.form.get('name')
            
            collection.delete_one({'ID':id})

            if created is None:
                created = datetime.now()

                
            update_data = {
                'ID': id, 
                'Expense-name': expName,
                'Expense-category': expCategory,
                'Amount': expAmount,
                'Expense-date': expDate,
                'CreatedAt': created,
                'UpdatedAt': datetime.now()
            }

            result = collection.insert_one(update_data)

            return render_template_string('''
                <script type="text/javascript">
                    alert('Expense updated successfully!');
                    window.location.href = "/";
                </script>
            ''')

    except Exception as e:
        return jsonify({'error': str(e)}), 500