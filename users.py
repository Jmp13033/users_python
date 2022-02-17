
from mysqlconnections import connectToMySQL # import mysqlconnections

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def all_users(cls):
        query = "SELECT * FROM users " # this is a SELECT query to do this.. 
        results = connectToMySQL ("users_schema").query_db(query)  # pass in the cls results
        users = []
        for user in results:
            users.append(cls(user))
        return users # return the value of the users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"
        result = connectToMySQL('users_schema').query_db(query,data)
        return result







