import os
SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

# create the database uri
class DatabaseURI:
    DATABASE_NAME = 'capstone'
    username = 'postgres'
    password = 'root'
    url = 'localhost:5432'
    SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}/{}".format(
        username, password, url, DATABASE_NAME)
