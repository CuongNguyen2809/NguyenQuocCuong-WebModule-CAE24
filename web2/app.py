from flask import Flask, render_template
app = Flask(__name__)

@app.route("/names")
def characters():
    name_list = ["Huy" , "Quan" , "Thai" ,"Nam" ,"Son"]
    return render_template("name.html",name_list=name_list)
 
c_list = [
        {
            "name" : "bun",
            "image" : "https://images.foody.vn/res/g25/245415/prof/s640x400/foody-mobile-bc-hg-jpg-699-636245617106542261.jpg",
            "link" : "https://www.dantri.com.vn",
            "ytid" : "oOnOHnjQk3w"
        },
        {
            "name" : "banh bao",
            "image" : "http://product.hstatic.net/1000267048/product/cadea_large.jpg",
            "link" : "http://thophat.com/",
            "ytid" : "gPy5"
        },
        {
            "name" : "pho ",
            "image" : "https://anh.24h.com.vn/upload/2-2016/images/2016-04-05/1459855054-1459854518-pho-chat-chem.jpg",
            "link" : "https://www.adayroi.com/banh-pho-viet-san-goi-300g-p-PRI21651",
            "ytid" : "WhishM2uX4s"
        }
    ]
@app.route("/food_items")
def food():

   
    return render_template("food.html", 
                            food_list = c_list)


@app.route("/food_detail/<int:index>")
def food_detail(index):
    food_item = c_list[index]
    return render_template("food_detail.html",a= food_item)


if __name__ =='__main__':
    app.run(debug=True)