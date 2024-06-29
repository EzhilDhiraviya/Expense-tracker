from .. import db as d
from .. import app
from flask import request , jsonify

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
        return jsonify(documents), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500