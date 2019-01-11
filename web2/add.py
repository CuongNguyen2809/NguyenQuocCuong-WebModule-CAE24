from flask import Flask,render_template,request
from models.character import Character
import mlab

mlab.connect()
app = Flask(__name__)


#Character.objects()

@app.route('/characters')
def characters():
    return render_template("characters.html")

@app.route('/add_character', methods=['GET','POST'])
def add_character():
     #1 gửi form (GET)
    if request.method == "GET":
        return  render_template("character_form.html")
    if request.method == "POST":
    
    
      #4 nhận form => lưu
        form = request.form
        name = form["name"]
        image = form ["image"]
        rate = form ["rate"]
        new_character = Character( name=name,image=image,rate=rate)
        new_character.save()

        return "Gotcha"




@app.route('/character')
def character():
    character_list = Character.objects()
    return render_template("characters.html",character_list=character_list)

@app.route("/character/<given_id>")
def character_detail(given_id):
    # character = Character.objects(id=given_id).first()
    character = Character.objects().with_id(given_id)

    if character is None:
        return "Not found" 
    else:
        return render_template("character_detail.html,",character=character)


if __name__ =='__main__':
    app.run(debug=True) 

    