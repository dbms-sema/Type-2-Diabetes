from flask import Flask, render_template, request
import pickle
from flask_sqlalchemy import SQLAlchemy
import numpy as np

# Load the Random Forest CLassifier model
filename = 'diabetes-prediction-rfc-model.pkl'
classifier = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

ENV = 'dev'

#if ENV == 'dev':
   # app.debug = True
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1430162@localhost/diabetes'
#else:
    #app.debug = False
   # app.config['SQLALCHEMY_DATABASE_URI'] = ''

#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
#db = SQLAlchemy(app)

class Details(db.Model):
    __tablename__ = 'details'
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    sex = db.Column(db.String(20))
    residence = db.Column(db.String(20))
    sbp = db.Column(db.Float)
    dbp = db.Column(db.Float)
    bmi = db.Column(db.Float)
    hypertension = db.Column(db.String(20))
    fhd = db.Column(db.String(20))
    alcohol = db.Column(db.String(20))
    smoker = db.Column(db.String(20))
    obesity = db.Column(db.String(20))
    physically_inactive = db.Column(db.String(20))

    def __init__(self,age,sex,residence,sbp,dbp,bmi,hypertension,fhd,alcohol,smoker,obesity,physically_inactive):
        self.age = age
        self.sex = sex
        self.residence = residence
        self.sbp =sbp
        self.dbp =dbp
        self.bmi = bmi
        self.hypertension = hypertension
        self.fhd = fhd
        self.alcohol = alcohol
        self.smoker = smoker
        self.obesity = obesity
        self.physically_inactive = physically_inactive


@app.route('/')

def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        age = request.form['age']
        sex = request.form['sex']
        residence = request.form['residence']
        sbp = request.form['sbp']
        dbp = request.form['dbp']
        bmi = request.form['bmi']
        hypertension = request.form['hypertension']
        fhd = request.form['fhd']
        alcohol = request.form['alcohol']
        smoker= request.form['smoker']
        obesity = request.form['obesity']
        physically_inactive = request.form['physically_inactive']
        if age == '' or sex =='' or residence == '' or sbp == '' or dbp == '' or bmi =='' or hypertension=='' or fhd =='' or alcohol=='' or smoker=='' or obesity =='' or physically_inactive =='':
            return render_template('index.html', message='<b>Please All Fields Must Be Filled In !!</b>')
        else:
            data = Details(age,sex,residence,sbp,dbp,bmi,hypertension,fhd,alcohol,smoker,obesity,physically_inactive)
            #db.session.add(data)
            #db.session.commit()
            data = np.array([[age,sex,residence,sbp,dbp,bmi,hypertension,fhd,alcohol,smoker,obesity,physically_inactive]])
            my_prediction = classifier.predict(data)
            return render_template('result.html', prediction=my_prediction)

if __name__ =='__main__':
     app.run()



