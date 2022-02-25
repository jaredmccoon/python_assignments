from flask import render_template,redirect,request,session,flash

from flask_app import app

from flask_app.models.favorite import Favorite
from flask_app.models.book import Book
from flask_app.models.author import Author



@app.route('/authors/<int:id>')
def authfavs(id):
    books = Book.get_all()
    favbooks = Favorite.get_favorites_by_author({'author_id':id})
    author = Author.get_one({'id':id})
    return render_template('authors_favorite.html', books=books, favbooks=favbooks, author=author)


@app.route('/books/<int:id>')
def favoritebook(id):
    book = Book.get_one({'id':id})
    authors = Author.get_all()
    favauthors = Favorite.get_one_by_book({'book_id':id})
    return render_template('books_favorite.html', authors=authors, favauthors=favauthors,book=book)

@app.route('/authors/<int:id>/add', methods=['POST'])
def newbookfav(id):
    data = {
        **request.form,
        'author_id': id
    }
    Favorite.save(data)
    return redirect('/')

@app.route('/books/<int:id>/add', methods=['POST'])
def newauthfav(id):
    data = {
        **request.form,
        'book_id': id
    }
    Favorite.save(data)
    return redirect(f'/books/{id}')