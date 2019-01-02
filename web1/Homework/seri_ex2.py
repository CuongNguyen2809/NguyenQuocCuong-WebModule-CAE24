from flask import Flask , render_template

app = Flask(__name__)

@app.route("/user/<username>")
def user(username):
    user_name ={
        "c1" : {
            "name" : "Nguyễn Văn A",
            "gender" : "Men",
            "age" : "18",
            "hobbies" : "music"
        },
        "c2" : {
            "name" : "Nguyễn Thị B",
            "gender" : "Female",
            "age" : "20",
            "hobbies" : "read book"
        },
        "c3" : {
            "name" : "Nguyễn Văn C",
            "gender" : "Men",
            "age" : "21",
            "hobbies" : "game"
        }
    }
    return render_template("user.html",user_name=user_name ,username=username)

if __name__ == "__main__":
    app.run(debug=True)
