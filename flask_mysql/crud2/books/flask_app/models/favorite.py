from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.book import Book
from flask_app.models.author import Author

class Favorite:
    def __init__(self, data):
        self.id = data['id']
        self.author_id = data['author_id']
        self.book_id = data['book_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_favorites_by_author(cls,data):
        query = "SELECT * FROM favorites LEFT JOIN books ON book_id = books.id WHERE author_id = %(author_id)s;"
        result = connectToMySQL('book_favorites').query_db(query,data)
        print(result)
        books = []
        for n in result:
            dict = {
                **n,
                'id':n['books.id']
            }

            books.append( Book(dict) )
        return books


    @classmethod
    def get_one_by_book(cls,data):
        query = "SELECT * FROM favorites LEFT JOIN authors ON author_id = authors.id WHERE book_id = %(book_id)s;"
        result = connectToMySQL('book_favorites').query_db(query,data)
        print(result)
        books = []
        for n in result:
            dict = {
                **n,
                'id':n['authors.id']
            }

            books.append( Author(dict) )
        return books



    @classmethod
    def save(cls, data):
        query = "INSERT INTO favorites (author_id,book_id) VALUES (%(author_id)s, %(book_id)s);"
        result = connectToMySQL('book_favorites').query_db(query, data)
        return result