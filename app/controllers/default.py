from app import app
from flask import render_template, request, flash


@app.route('/hello')
def index():
    flash("Qual é seu nome ?" )
    return render_template('index.html')

@app.route("/greet", methods=['POST', 'GET'])
def greet():
    flash("Olá " + str(request.form['name_input']) + ", prazer em te conhecer !")
    return render_template('index.html')

