from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_one(cls):
        query = "SELECT * FROM dojos WHERE id = %(uid)s;"
        results = connectToMySQL('dojo_survey_schema').query_db(query)
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"
        result = connectToMySQL('dojo_survey_schema').query_db(query, data)
        return result

    @staticmethod
    def validator(form_data):
        is_valid = True

        if len(form_data['name']) < 2:
            is_valid = False
            flash("name is required", "err_dojo_name")

        if len(form_data['location']) == False:
            is_valid = False
            flash("location is required", "err_dojo_location")

        if len(form_data['language']) == False:
            is_valid = False
            flash("language is required", "err_dojo_language")

        if len(form_data['comment']) == False:
            is_valid = False
            flash("comment is required", "err_dojo_comment")


        return is_valid