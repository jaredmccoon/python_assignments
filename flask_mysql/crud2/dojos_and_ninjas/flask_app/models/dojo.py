from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]



    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos_and_ninjas_schema.dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        for u in results:
            dojos.append( cls(u) )
        return dojos

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos_and_ninjas_schema.dojos (name) VALUES (%(name)s);"

        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return result

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos_and_ninjas_schema.dojos WHERE id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return cls(result[0])
