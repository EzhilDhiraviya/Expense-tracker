from .. import db as d
from .. import app
from flask import request, jsonify, render_template

@app.post('/fetchCategory')
def fetchCategory():
    try:
        category = request.form.get("category")
        collection = d.db['user-exp-collection']
        cursor = collection.find({'Expense-category': category})
        
        expenses = []
        for doc in cursor:
            doc.pop('_id', None)
            expenses.append(doc)
        
        return render_template('fetchAll.html', expenses=expenses)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
