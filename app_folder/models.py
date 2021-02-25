from datetime import datetime
from flask_login import UserMixin

from app_folder import db, login_manager


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1024), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # date = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __init__(self, text, tags):  #, date):
        self.text = text.strip()
        self.tags = [Tag(text=tag.strip()) for tag in tags.split(',')]
#


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(32), nullable=False)

    message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False)
    message = db.relationship('Message', backref=db.backref('tags', lazy=True))


class Users(db.Model, UserMixin):

    # __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    # email = db.Column(db.String, nullable=True, unique=True)
    #
    # description = db.Column(db.String, nullable=True, unique=True)


@login_manager.user_loader
def load_user(user_id):
    # return Users.query.get(user_id)
    print("User_ID: ", Users.query.filter_by(id=user_id).first())
    return Users.query.filter_by(id=user_id).first()

# def user_loader(id):
#     return User.query.filter_by(id=id).first()
