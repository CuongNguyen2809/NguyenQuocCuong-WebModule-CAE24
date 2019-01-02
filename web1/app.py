from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") #router
def home(): #view function
    c = {
        "name" : "AQUAMAN",
        "company" : "DC----Comis",
        "image" : "https://img-s-msn-com.akamaized.net/tenant/amp/entityid/BBR5AJs.img?h=314&w=624&m=6&q=60&o=f&l=f&x=1759&y=527",
        "abilities" : ["Speed","Strength","Reflexes"]
    }

   
    return render_template("home.html", 
                            character=c)
    
@app.route("/c4e")
def c4e():
    return "Code For Everyone 24"


@app.route("/hi/<name>")
def sayhi(name):
    print(name)
    return "Hi " + name

@app.route("/add/<int:a>/<int:b>")
def add(a , b):
    s = a + b
    return str(s)

    
  

if __name__ == "__main__":
    app.run(debug=True)