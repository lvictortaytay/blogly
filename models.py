"""Models for Blogly."""
from enum import unique
import datetime 
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


class Post(db.Model):
    """post table"""
    __tablename__ = "posts"

    id = db.Column(db.Integer , primary_key = True)
    title = db.Column(db.String(50) , nullable = False)
    content = db.Column(db.Text , nullable = False)
    created_at = db.Column(db.DateTime , nullable = False , default = datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id' , ondelete = "CASCADE"), nullable=False)


