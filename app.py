import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle



#Create the flask app
app = Flask(__name__, template_folder= 'templates')

# Load the pickle models
model1= pickle.load(open("model1.pkl", "rb")) # Time invariant model
model2= pickle.load(open("model2.pkl", "rb")) # Time variant model
#model3= pickle.load(open("model3.pkl", "rb")) # Multivariable model



@app.route("/")
def index():
    return render_template('index.html')


@app.route("/forecast", methods= ['GET'])
def forecast():
    months = int(request.form['month'])
    model_to_choose= int(request.form['model'])

    if model_to_choose == 1:
        result= model1.predict(months)

    elif model_to_choose == 2:
        result= model2.predict(months)
   # else:
    #    result= model3.predict(months)

        return render_template("forecast.html")





if __name__ == '__main__':
   app.run(debug= True)