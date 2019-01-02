from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/about-me")
def aboutme():
    c = {
        "name": "Nguyen Quoc Cuong",
        "work": "student",
        "school": "BK university",
        "hobbies": ["game","football"]  
    }
    return render_template("information.html", ch = c)

@app.route("/school")
def school():
    return redirect("https://techkids.vn/")

if __name__ == "__main__":
    app.run(debug=True)