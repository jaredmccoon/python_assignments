from flask import render_template, redirect, request, session, flash
from flask_app import app, bcrypt
from flask_app.models.user import User
from flask_app.models.recipe import Recipe


@app.route('/recipes/<int:id>')
def show(id):
    recipe = Recipe.get_one({'id':id})
    data = {
        'id': session['userid']
    }
    user = User.get_one(data)
    return render_template('recipe.html', recipe=recipe, user=user)

@app.route('/recipes/add')
def newrecipe():
    data = {
        'id': session['userid']
    }
    user = User.get_one(data)
    return render_template('new_recipe.html',user=user)

@app.route('/recipe/edit/<int:id>')
def editrecipe(id):
    data = {
        'id': session['userid']
    }
    user = User.get_one(data)
    recipe = Recipe.get_one({'id':id})
    return render_template('edit_recipe.html', recipe=recipe, user=user)


@app.route('/recipe/create', methods=['POST'])
def addrecipe():
    Recipe.save(request.form)
    return redirect('/dashboard')

@app.route('/recipe/update', methods=['POST'])
def changerecipe():
    Recipe.update_one(request.form)
    return redirect('/dashboard')

@app.route('/recipe/delete/<int:id>')
def delete(id):
    Recipe.destroy({'id':id})
    return redirect('/dashboard')