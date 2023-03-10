"""Models for Blogly."""
from enum import unique
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

default = "https://sbcf.fr/wp-content/uploads/2018/03/sbcf-default-avatar.png"


class User(db.Model):
    """user table"""
    __tablename__ = "users"


    id = db.Column(db.Integer , primary_key = True , autoincrement = True)
    first_name = db.Column(db.Text , nullable = False)
    last_name = db.Column(db.Text)
    image_url = db.Column(db.String , nullable = False , server_default = "https://sbcf.fr/wp-content/uploads/2018/03/sbcf-default-avatar.png")
