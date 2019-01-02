from flask import Flask 

app = Flask(__name__)

@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight,height):

    BMI = weight/((height/100)**2)
    if BMI < 16:
        return (" BMI : " + str(BMI) + "Severely underweight")
    elif  16 <= BMI < 18.5:
        return (" BMI : " + str(BMI) + "Underweight")
    elif  18.5 <= BMI < 25:
        return (" BMI : " + str(BMI) + "Normal")
    elif  25 <= BMI < 30:
        return (" BMI : " + str(BMI) + "Overweight")
    elif BMI > 30:
        return (" BMI : " + str(BMI) + "Obese")
        

if __name__ == "__main__":
    app.run(debug=True)



