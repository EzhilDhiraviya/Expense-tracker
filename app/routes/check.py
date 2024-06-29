from .. import app
from flask import request , render_template

@app.route('/check', methods=['GET'])
def show_add_form():
    return render_template('add.html')
