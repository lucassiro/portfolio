from operator import methodcaller
from flask import Blueprint
from flask import render_template, request, redirect
from models import User
from database import db

bp_users = Blueprint("users", __name__, template_folder="templates")

@bp_users.route("/create", methods=["GET", "POST"])
def create():
    if request.method=="GET":
        return render_template("users_create.html")

    if request.method=="POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        cpassword = request.form.get("cpassword")

        user = User(name, email, password)
        db.session.add(user)
        db.session.commit()
        return "OK"

@bp_users.route("/recovery")
def recovery():
    users = User.query.all()
    return render_template("users_recovery.html", users=users)

@bp_users.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    user = User.query.get(id)

    if request.method == "GET":
        return render_template("users_update.html", user = user)
    
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        name = request.form.get("name")
        user.name = name
        user.email = email
        db.session.add(user)
        db.session.commit()
        return redirect("/users/recovery")

@bp_users.route("/delete/<int:id>", methods=["GET", "POST"])
def delete(id):
    user = User.query.get(id)

    if request.method == "GET":
        return render_template("users_delete.html", user = user)
    
    if request.method == "POST":
        db.session.delete(user)
        db.session.commit()
        return "deleted"
