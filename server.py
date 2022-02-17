from flask import Flask, render_template, request, redirect
app=Flask(__name__)
from users import User


@app.route("/")
def home():
    return redirect("/userpage")


@app.route("/create",)
def new_user():
    return render_template("new_user.html")




@app.route("/user/make", methods = ["POST"])
def make_user():
    User.save(request.form)

    return redirect("/userpage" )



@app.route("/userpage")
def users():
    return render_template("index.html", users = User.all_users()) 





























if __name__=="__main__":
    app.run(debug=True, port=5001)
