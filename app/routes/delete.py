from .. import db as d
from .. import app
from flask import request , jsonify, render_template, render_template_string

@app.post('/deleteID')
def deleteID():
    try:
        id = request.form.get('ID')
        collection=d.db['user-exp-collection']
        collection.delete_one({'ID':id})
        return render_template_string('''
                <script type="text/javascript">
                    alert('Expense deleted successfully!');
                    window.location.href = "/";
                </script>
            ''')
    except Exception as e:
        return jsonify({'error': str(e)}), 500