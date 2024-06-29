from .. import db as d
from .. import app
from flask import request , jsonify, render_template

@app.post('/fetch')
def fetch():
    try:
        data=request.get_json()
        id=data.get("ID")
        collection=d.db['user-exp-collection']
        cursor=collection.find({'ID':id})
        documents=[]
        for doc in cursor:
            doc['CreatedAt'] = doc['CreatedAt'].as_datetime()
            doc['UpdatedAt'] = doc['UpdatedAt'].as_datetime()
            doc.pop('_id',None)
            documents.append(doc)
        print(documents)
        return render_template('results.html', documents=documents)
        # return jsonify(documents)

    except Exception as e:
        return jsonify({'error': str(e)}), 500