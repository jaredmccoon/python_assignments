from flask import render_template, redirect, request, session, flash
from flask_app import app, bcrypt
from flask_app.models.user import User
from flask_app.models.recipe import Recipe


@app.route('/')
def index():
    if 'userid' in session:
        return redirect('/dashboard')
    return render_template("register_login.html")

@app.route('/user/login', methods=['POST'])
def login():
    is_valid = User.validator_login(request.form)

    if not is_valid:
        return redirect('/')
        
    return redirect('/dashboard')

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
    return redirect('/dashboard')


@app.route('/dashboard')
def success():
    if 'userid' not in session:
        return redirect('/')
    data = {
        'id': session['userid']
    }
    recipes = Recipe.get_all()
    user = User.get_one(data)
    return render_template('dashboard.html', recipes=recipes, user=user)

@app.route('/logout')
def logout():
    del session['userid']
    return redirect('/')