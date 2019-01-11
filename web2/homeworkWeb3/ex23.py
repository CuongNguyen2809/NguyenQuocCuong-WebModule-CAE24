from flask import Flask,render_template,request
from models.river import River
import mlab_ex

mlab_ex.connect()
app = Flask(__name__)
# Ex2
@app.route('/river/Africa')
def river():
    name_list = River.objects(continent="Africa")
    return render_template("ex23.html",name_list=name_list)

# Ex3
@app.route('/river/America')
def river_america():
    name_list = River.objects(continent="S. America",length__lt=1000)
    return render_template("ex23.html",name_list=name_list)

if __name__ == "__main__":
    app.run(debug=True)
