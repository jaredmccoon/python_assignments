from flask import render_template,redirect,request,session,flash

from flask_app import app

from flask_app.models.book import Book
from flask_app.models.author import Author


@app.route('/books')
def newbook():
    books = Book.get_all()
    return render_template('new_book.html', books=books)

@app.route('/books/create', methods=['POST'])
def addbook():
    Book.save(request.form)
    return redirect('/books')

# @app.route('/books/<int:id>')
# def bookfavs(id):
#     book = Book.get_one({'id':id})
#     authors = Author.get_all()
#     return render_template('books_favorite.html', book=book, authors=authors)

# @app.route('/books/<int:id>/add', methods=['POST'])
# def newauthorfav():
#     return redirect('/books/<int:id>')