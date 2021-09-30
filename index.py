from flask import flask

from flask import Flask,render_template

app = Flask(__name__)

""" AQUI NUESTRAS ROUTAS DE NUESTRO CRUD-API """
""" HERE GET ROUTES CRUD-API """
@app.route('/')
def index():
    return ('hello world!')

@app.route('/layout')
def layout():
    return render_template('layout.html')


    print('the server is running again')


if __name__== '__main__':
    app.run(debug=True)