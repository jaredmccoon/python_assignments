from flask_app.config.mysqlconnection import connectToMySQL


class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL('book_favorites').query_db(query)
        books = []
        for n in results:
            books.append( cls(n) )
        return books

    @classmethod
    def save(cls, data):
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s,%(num_of_pages)s);"
        result = connectToMySQL('book_favorites').query_db(query, data)
        return result 

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM books WHERE id = %(id)s;"
        result = connectToMySQL('book_favorites').query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_many(cls, data):
        query = "SELECT * FROM books WHERE id = %(id)s;"
        result = connectToMySQL('book_favorites').query_db(query, data)
        favs = []
        for n in favs:
            favs.append( cls(n) )
        return favs

