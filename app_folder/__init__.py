from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.secret_key = 'SECRET_KEY=S3cr3t_Key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://leon:ResidentEvil@localhost/leons_psql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Upload configuration
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024    # 2Mb
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'app_folder/static/upload_folder/avatar'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
# login_manager.init_app(app)

from app_folder import models, routes

db.create_all()
