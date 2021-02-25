<<<<<<< HEAD
from flask import Flask, render_template, request
import pickle
from flask_sqlalchemy import SQLAlchemy
import numpy as np

# Load the Random Forest CLassifier model
filename = 'diabetes-prediction-rfc-model.pkl'
classifier = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = False
    app.config['DATABASE_URL'] = ''
else:
    app.debug = True
    app.config['DATABASE_URL'] = 'postgres://wmelfswyfwfynk:14fb51e0f1a8e67ec22ada0ed28024e921f8ce95ebc31a198a430aacf02fbc1e@ec2-3-209-176-42.compute-1.amazonaws.com:5432/d3v0q99e4734em'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =True
db = SQLAlchemy(app)

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
            db.session.add(data)
            db.session.commit()
            data = np.array([[age,sex,residence,sbp,dbp,bmi,hypertension,fhd,alcohol,smoker,obesity,physically_inactive]])
            my_prediction = classifier.predict(data)
            return render_template('result.html', prediction=my_prediction)

if __name__ =='__main__':
     app.run()



=======
from flask import Flask, render_template, request
import pickle
from flask_sqlalchemy import SQLAlchemy
import numpy as np

# Load the Random Forest CLassifier model
filename = 'diabetes-prediction-rfc-model.pkl'
classifier = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = False
    app.config['DATABASE_URL'] = ''
else:
    app.debug = True
    app.config['DATABASE_URL'] = 'postgres://wmelfswyfwfynk:14fb51e0f1a8e67ec22ada0ed28024e921f8ce95ebc31a198a430aacf02fbc1e@ec2-3-209-176-42.compute-1.amazonaws.com:5432/d3v0q99e4734em'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =True
db = SQLAlchemy(app)

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
            db.session.add(data)
            db.session.commit()
            data = np.array([[age,sex,residence,sbp,dbp,bmi,hypertension,fhd,alcohol,smoker,obesity,physically_inactive]])
            my_prediction = classifier.predict(data)
            return render_template('result.html', prediction=my_prediction)

if __name__ =='__main__':
     app.run()



>>>>>>> 7b924532a7e768e5d164d301dd7324282b483d8d
