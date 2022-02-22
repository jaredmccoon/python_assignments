from flask import render_template, redirect, request, session
from flask_app import app, bcrypt
from flask_app.models.model import User


@app.route('/')
def index():
    if 'user' in session:
        return redirect('/success')
    return render_template("register.html")

@app.route('/user/login', methods=['POST'])
def login():
    is_valid = User.validator_login(request.form)

    if not is_valid:
        return redirect('/login')
        
    return redirect('/success')

@app.route('/user/create', methods=['POST'])
def create_user():
    is_valid = User.validator(request.form)

    if is_valid == False:
        return redirect('/')
    
    hash_pw = bcrypt.generate_password_hash(request.form['password'])

    data = {
        **request.form,
        'password': hash_pw
    }

    id = User.save(data)
    session['userid'] = id
    return redirect('/success')

@app.route('/login')
def newlogin():
    return render_template('login.html')

@app.route('/success')
def success():
    if 'userid' not in session:
        return redirect('/')
    return render_template('success.html')

@app.route('/logout')
def logout():
    del session['userid']
    return redirect('/login')