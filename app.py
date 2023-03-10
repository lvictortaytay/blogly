"""Blogly application."""

from pydoc import render_doc
from flask import Flask, redirect, render_template,request
from models import db, connect_db , User , default

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()


@app.route("/")
def homePage():
    users = User.query.all()
    return render_template("home.html" , users = users)


@app.route("/addUser")
def addUserPage():
    return render_template("newUser.html")




@app.route("/createUser" , methods = ["POST"])
def createUser():
    first_name = request.form["firstName"]
    last_name = request.form["lastName"]
    if request.form["imageUrl"] != '':
        image_url = request.form["imageUrl"]
    else:
        image_url = default
    newUser = User(first_name = first_name , last_name = last_name , image_url = image_url)
    db.session.add(newUser)
    db.session.commit()
    return redirect("/")


@app.route("/editUser/<int:user_id>")
def editUser(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("editUser.html" , user = user)


@app.route("/userDetails/<int:user_id>", methods = ["POST"])
def updateUser(user_id):
    user = User.query.get_or_404(user_id)
    user.first_name = request.form["firstName"]
    user.last_name = request.form["lastName"]
    user.image_url = request.form["imageUrl"]

    db.session.add(user)
    db.session.commit()
    return redirect("/")


@app.route("/userDetail/<int:user_id>")
def userDetailPage(user_id):
    user = User.query.get(user_id)
    return render_template("userDetail.html", user = user)

@app.route("/deleteUser/<int:user_id>", methods = ["POST"])
def deleteUser(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect("/")
