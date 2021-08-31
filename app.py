from flask import Flask, render_template, request
import pickle
from flask_sqlalchemy import SQLAlchemy
import numpy as np

# Load the Random Forest CLassifier model
filename = 'diabetes-prediction-rfc-model.pkl'
classifier = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

ENV = 'dev'

# if ENV != 'dev':
#     app.debug = False
#     app.config['DATABASE_URL'] = ''
# else:
app.debug = True
app.config['DATABASE_URI'] = os.environ.get('postgres://mvkwzjbntalnko:365226844a4af9cc89bff9a45e6bf57ae3f91d5ceb9dca919bb608628cf706e2@ec2-52-203-74-38.compute-1.amazonaws.com:5432/d5b2hjlk5kkf9')


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Details(db.Model):
    __tablename__ = 'details'
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    sex = db.Column(db.String(20))
    residence = db.Column(db.String(20))
    bmi = db.Column(db.Float)
    alcohol = db.Column(db.String(20))
    smoker = db.Column(db.String(20))
    sbp = db.Column(db.Float)
    fhd = db.Column(db.String(20))
    hypertension = db.Column(db.String(20))
    dbp = db.Column(db.Float)
    obesity = db.Column(db.String(20))
    physically_inactive = db.Column(db.String(20))

    def __init__(self,age,sex,residence,bmi,alcohol,smoker,sbp,fhd,hypertension,dbp,obesity,physically_inactive):
        self.age = age
        self.sex = sex
        self.residence = residence
        self.bmi = bmi
        self.alcohol = alcohol
        self.smoker = smoker
        self.sbp = sbp
        self.fhd = fhd
        self.hypertension = hypertension
        self.dbp = dbp
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
        bmi = request.form['bmi']
        alcohol = request.form['alcohol']
        smoker= request.form['smoker']
        sbp = request.form['sbp']
        fhd = request.form['fhd']
        hypertension = request.form['hypertension']
        dbp = request.form['dbp']
        obesity = request.form['obesity']
        physically_inactive = request.form['physically_inactive']
        if age == '': 
            return render_template('index.html', message='<b>Please All Fields Must Be Filled In !!</b>')
        if sex =='': 
            return render_template('index.html', message='<b>Please All Fields Must Be Filled In !!</b>')               
        if residence == '':
            return render_template('index.html', message='<b>Please All Fields Must Be Filled In !!</b>')
        if bmi =='':
            return render_template('index.html', message='<b>Please All Fields Must Be Filled In !!</b>')
        if alcohol=='':
            return render_template('index.html', message='<b>Please All Fields Must Be Filled In !!</b>')
        if smoker=='':
            return render_template('index.html', message='<b>Please All Fields Must Be Filled In !!</b>')
        if sbp == '':
            return render_template('index.html', message='<b>Please All Fields Must Be Filled In !!</b>')
        if fhd =='':
            return render_template('index.html', message='<b>Please All Fields Must Be Filled In !!</b>')
        if hypertension=='':
            return render_template('index.html', message='<b>Please All Fields Must Be Filled In !!</b>')
        if dbp == '':
            return render_template('index.html', message='<b>Please All Fields Must Be Filled In !!</b>')
        if obesity =='':
            return render_template('index.html', message='<b>Please All Fields Must Be Filled In !!</b>')
        if physically_inactive =='':
            return render_template('index.html', message='<b>Please All Fields Must Be Filled In !!</b>')
        else:
            data = Details(age,sex,residence,bmi,alcohol,smoker,sbp,fhd,hypertension,dbp,obesity,physically_inactive)
            db.create_all()
            db.session.add(data)
            db.session.commit()
            data = np.array([[age,sex,residence,bmi,alcohol,smoker,sbp,fhd,hypertension,dbp,obesity,physically_inactive]])
            my_prediction = classifier.predict(data)
            return render_template('result.html', prediction=my_prediction)

if __name__ =='__main__':
     app.run()



