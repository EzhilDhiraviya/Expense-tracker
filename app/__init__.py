from flask import Flask,render_template
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

from .routes import add, fetchAll, delete, update, fetchCategory, fetchMonth

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/category')
def category():
    return render_template('category.html')

if __name__ == '__main__':
    app.run(debug=True) 