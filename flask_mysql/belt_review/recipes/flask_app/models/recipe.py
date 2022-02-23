from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash, session
from flask_app import bcrypt, DATABASE


class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.umin = data['umin']
        self.date = data['date']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM list_of_recipes JOIN users on users.id = user_id;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM list_of_recipes WHERE id = %(id)s"
        result = connectToMySQL(DATABASE).query_db(query,data)
        if result:
            return cls(result[0]) 
        return False

    @classmethod
    def save(cls,data):
        query = "INSERT INTO list_of_recipes (name,description,instructions,umin,date,user_id) VALUES (%(name)s,%(description)s,%(instructions)s,%(umin)s,%(date)s,%(user_id)s);"
        recipe = connectToMySQL(DATABASE).query_db(query,data)
        return recipe

    @classmethod
    def update_one(cls, data):
        query = "UPDATE list_of_recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, umin = %(umin)s, date = %(date)s, updated_at=NOW()  WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM list_of_recipes WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query,data)

    # @staticmethod
    # def validator(form_data):
    #     is_valid = True

    #     if len(form_data['first_name']) < 2:
    #         is_valid = False
    #         flash("name is required", "err_first_name")

    #     return is_valid