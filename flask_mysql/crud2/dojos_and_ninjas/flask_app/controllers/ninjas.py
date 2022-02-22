from flask import render_template,redirect,request,session,flash

from flask_app import app

from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def newninja():
    return render_template('new_ninja.html', dojos = Dojo.get_all())

@app.route('/ninja/save', methods=['POST'])
def returnninja():
    print(request.form)
    Ninja.save(request.form)
    return redirect('/')