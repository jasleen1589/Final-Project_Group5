
import string
import flask
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from flask_cors import CORS
import flask_cors
import numpy as np
from requests import session
from joblib import load
import pickle


# Load the model
model3 = load('Resources/heart-randomForest1-knn-model.pkl')
#################################################
# Flask Setup
#################################################

app = flask.Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

#################################################
# Flask Routes
#################################################

@app.route("/" )
def homepage():    
     return flask.render_template('homepage.html')
    

@app.route("/charts")
def charts():
     return flask.render_template("charts.html")
  
@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':												
         sex = int(request.form['sex'])
         age = request.form.get('age')
         education = request.form.get('education')
         currentSmoker = int(request.form['currentSmoker'])
         cigsPerDay = int(request.form['cigsPerDay'])
         BPMeds = request.form.get('BPMeds')
         prevalentStroke = int(request.form['prevalentStroke'])
         prevalentHyp = int(request.form['prevalentHyp'])
         diabetes = request.form.get('diabetes')
         totChol = float(request.form['totChol'])
         sysBP = request.form.get('sysBP')
         diaBP = int(request.form['diaBP'])
         BMI = request.form.get('BMI')
         heartRate = request.form.get('heartRate')
         glucose = float(request.form['glucose'])
        

         data = np.array([[sex,age,education,currentSmoker,cigsPerDay,BPMeds,prevalentStroke,prevalentHyp,diabetes,totChol,sysBP,diaBP,BMI,heartRate,glucose]])
         data_df = pd.DataFrame(data, columns=['sex','age','education','currentSmoker','cigsPerDay','BPMeds','prevalentStroke','prevalentHyp','diabetes','totChol','sysBP','diaBP','BMI','heartRate','glucose'])
																		

         print(data_df)
         my_prediction = model3.predict(data_df)  
       
         return render_template('result.html', prediction=my_prediction)
    else:
         # Placeholder response for GET request
       return flask.render_template("predict.html")
    

    

if __name__ == '__main__':
    # //app.run(debug=True)
    import os

    port = 5000

    # Open a web browser pointing at the app.
    os.system("open http://localhost:{0}".format(port))

    # Set up the development server on port 8000.
    app.debug = True
    app.run(port=port)
