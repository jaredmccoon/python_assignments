from flask import render_template,redirect,request,session,flash

from flask_app import app

from flask_app.models.dojo import Dojo

@app.route('/')          
def hello_world():
    return render_template('index.html') 

@app.route('/result', methods=['POST'])
def result():
    is_valid = Dojo.validator(request.form)

    if not is_valid:
        return redirect('/')

    session['result'] = request.form

    Dojo.save(request.form)
    return redirect('/results')

@app.route('/results')
def show():
    dojo = session['result']
    return render_template('result.html', dojo=dojo)
