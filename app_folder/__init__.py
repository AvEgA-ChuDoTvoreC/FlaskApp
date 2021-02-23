from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://leon:ResidentEvil@localhost/leons_psql'
db = SQLAlchemy(app)

