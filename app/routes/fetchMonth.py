from .. import db as d
from .. import app
from flask import request, jsonify, render_template
from datetime import datetime

@app.post('/fetchMonth')
def fetch_month_year():
    # try:
        month = int(request.form.get("month"))  
        year = int(request.form.get("year"))

        start_date = datetime(year, month, 1)
        end_date = datetime(year, month + 1 if month < 12 else 1, 1)  

        collection = d.db['user-exp-collection']
        cursor = collection.find({
            'Expense-date': {
                '$gte': start_date,
                '$lt': end_date
            }
        })

        expenses = []
        for doc in cursor:
            doc.pop('_id', None)
            expenses.append(doc)

        return render_template('fetchAll.html', expenses=expenses)

    # except Exception as e:
    #     return jsonify({'error': str(e)}), 500
