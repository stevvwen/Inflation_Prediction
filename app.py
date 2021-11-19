import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle



#Create the flask app
app = Flask(__name__, template_folder='templates')

# Load the pickle models
model1= pickle.load(open("model1.pkl", "rb")) # Time invariant model
model2= pickle.load(open("model2.pkl", "rb")) # Time variant model
model3= pickle.load(open("model3.pkl", "rb")) # Multivariable model



@app.route("/", methods= ['GET'])
def index():
    return render_template('index.html')


@app.route("/", methods= ['POST'])
def forecast():
    months_to_forecast= request.form.values

    return render_template("index.html")




if __name__ == '__main__':
   app.run()