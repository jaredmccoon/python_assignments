from flask import render_template,redirect,request,session,flash

from flask_app import app

from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def hello_world():
    return redirect('/dojos')

@app.route('/dojos')
def newdojo():
    return render_template('new_dojo.html',dojos = Dojo.get_all())

@app.route('/dojos', methods=['POST'])
def returndojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def showdojo(id):
    ninjas = Ninja.get_all({'id': id})
    return render_template('show_dojo.html', ninjas = ninjas)

