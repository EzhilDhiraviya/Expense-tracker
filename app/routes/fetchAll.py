from .. import db as d
from .. import app
from flask import request , jsonify, render_template

@app.get('/fetchAll')
def fetchAll():
    
        collection = d.db['user-exp-collection']
        expenses = list(collection.find())

        # Convert MongoDB ObjectId to string
        for expense in expenses:
            expense['_id'] = str(expense['_id'])

        return render_template('fetchAll.html', expenses=expenses)

    # except Exception as e:
    #     return jsonify({'error': str(e)}), 500