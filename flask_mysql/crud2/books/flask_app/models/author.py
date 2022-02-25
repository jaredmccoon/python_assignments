from flask_app.config.mysqlconnection import connectToMySQL


class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors"
        results = connectToMySQL('book_favorites').query_db(query)
        authors = []
        for n in results:
            authors.append( cls(n) )
        return authors


    @classmethod
    def save(cls, data):
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        result = connectToMySQL('book_favorites').query_db(query, data)
        return result 

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM authors WHERE id = %(id)s;"
        result = connectToMySQL('book_favorites').query_db(query, data)
        return cls(result[0])