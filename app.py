
import string
import flask
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from flask_cors import CORS
import flask_cors
import numpy as np
from requests import session

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func,literal_column
from sqlalchemy import desc
from sqlalchemy.sql.expression import case

from flask import Flask, jsonify

import pickle




# Load the Random Forest CLassifier model
filename = 'Resources/heart-prediction-knn-model.pkl'
model = pickle.load(open(filename, 'rb'))
 




#################################################
# Flask Setup
#################################################

app = flask.Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

#################################################
# Flask Routes
#################################################

@app.route("/")
def homepage():
    return flask.render_template("homepage.html")
    

@app.route("/charts")
def charts():
     return flask.render_template("charts.html")
    
@app.route("/thanks")
def thanks():
     return flask.render_template("thanks.html")
    


@app.route('/predict', methods=['GET','POST'])

def predict():
    if request.method == 'POST':

        age = int(request.form['age'])
        sex = request.form.get('sex')
        chestpain = request.form.get('cp')
        restbp = int(request.form['trestbps'])
        chol = int(request.form['chol'])
        fbs = request.form.get('fbs')
        restecg = int(request.form['restecg'])
        maxhr = int(request.form['thalach'])
        exang = request.form.get('exang')
        oldpeak = float(request.form['oldpeak'])
        slope = request.form.get('slope')
        ca = int(request.form['ca'])
        thal = request.form.get('thal')
        
        data = np.array([[age,sex,chestpain,restbp,chol,fbs,restecg,maxhr,exang,oldpeak,slope,ca,thal]])
        data_df = pd.DataFrame(data, columns=['age', 'sex', 'chestpain', 'restbp', 'chol', 'fbs', 'restecg', 'maxhr', 'exang', 'oldpeak', 'slope', 'ca', 'thal'])

        print(data_df)
        my_prediction = model.predict(data_df)  
             
        return render_template('result.html', prediction=my_prediction)
    else:
        # Placeholder response for GET request
        return render_template('predict.html')


    

if __name__ == '__main__':
    # //app.run(debug=True)
    import os

    port = 5000

    # Open a web browser pointing at the app.
    os.system("open http://localhost:{0}".format(port))

    # Set up the development server on port 8000.
    app.debug = True
    app.run(port=port)
