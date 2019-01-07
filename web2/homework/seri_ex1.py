from flask import Flask, render_template, request
from mongoengine import Document, StringField

class SignUp(Document):
    fullname = StringField()
    email = StringField()
    username = StringField()
    password = StringField()

app = Flask(__name__)

@app.route("/register", methods=["GET","POST"])
def sign_up():
    if request.method == "GET":
        return render_template("register.html")

    if request.method == "POST":
        post = SignUp(
            fullname = request.form["fullname"],
            email = request.form["email"],
            username = request.form["username"],
            password = request.form["password"]
        )
        post.save()
        return "successfully"


if __name__ == "__main__":
    app.run(debug=True)