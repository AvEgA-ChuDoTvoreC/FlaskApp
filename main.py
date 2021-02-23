#!flask/bin/python3
import time
import logging
from datetime import datetime
from collections import namedtuple

from flask import render_template, redirect, url_for, request

from app_folder import app, db

logging.basicConfig(level=logging.INFO)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1024), nullable=False)
    create_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # date = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __init__(self, text, tags):  #, date):
        self.text = text.strip()
        self.tags = [Tag(text=tag.strip()) for tag in tags.split(',')]
        # self.date = date
#

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(32), nullable=False)

    message_id = db.Column(db.Integer, db.ForeignKey('message.id'), nullable=False)
    message = db.relationship('Message', backref=db.backref('tags', lazy=True))


db.create_all()


@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['GET'])
def main():
    return render_template('main.html', messages=Message.query.all())


@app.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['text']
    tag = request.form['tag']

    if text:
        # messages.append(Messages(text, tag))
        db.session.add(Message(text, tag))  # , date))
        db.session.commit()
    elif tag and not text:
        pass

    return redirect(url_for('main'))


# while True:
try:
    app.run(host="0.0.0.0", port=5000, debug=True)
except KeyboardInterrupt:
    logging.info("The module was stopped")
except Exception as err:
    logging.exception("The module was failed {}".format(err))
finally:
    time.sleep(1)

# def url_for_(*args, **kwargs):
#     return '/update_agent' + url_for(*args, **kwargs)
#
# @app.context_processor
# def inject_stage_and_region():
#     return dict(url_for=url_for_)
