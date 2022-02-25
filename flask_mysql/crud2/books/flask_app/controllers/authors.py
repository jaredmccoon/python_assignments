from flask import render_template,redirect,request,session,flash

from flask_app import app

from flask_app.models.author import Author


@app.route('/')
def newpage():
    return redirect('/authors')

@app.route('/authors')
def newauthor():
    authors = Author.get_all()
    return render_template('new_author.html',authors=authors)

@app.route('/authors/create', methods=['POST'])
def addauthor():
    Author.save(request.form)
    return redirect('/authors')

# @app.route('/authors/<int:id>')
# def authorfav():
#     authors = Author.get_all()
#     return render_template('author_favorite.html', authors=authors)

