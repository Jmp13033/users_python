
from flask_app import app
from flask import render_template, sessions, redirect, request

from flask_app.models.user import User

@app.route("/")
def home():
    return redirect("/userpage")


@app.route("/create",)
def new_user():
    return render_template("new_user.html")



@app.route("/user/make", methods = ["POST"])
def make_user():
    User.save(request.form)
    return redirect("/userpage")




@app.route("/user/show/<int:id>")
def show(id):
    data = {
        "id": id

    }
    return render_template("show.html", user = User.get_one(data))




@app.route("/userpage")
def users():
    return render_template("index.html", users = User.all_users()) 



@app.route("/user/delete/<int:id>")
def delete(id):
    data = {
        "id": id
    }
    User.destroy(data)
    return redirect("/userpage")


@app.route("/user/edit/<int:id>")
def edit(id):
    data = {
        "id": id

    }
    return render_template("edit.html", user = User.get_one(data))



@app.route("/user/update", methods = ["POST"])
def update():
    User.update(request.form)
    return redirect("/userpage")