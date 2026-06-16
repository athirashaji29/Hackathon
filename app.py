from flask import Flask, render_template, request
import pickle
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.decomposition import PCA
scaler = StandardScaler()

app = Flask(__name__)
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)
# Load your machine learning model

@app.route('/')
def index():
    return render_template('index.html')
    # CALLING THE HOMEPAGE

def age(age):
    new_age=[]
    for i in age:
        if(i < 17):
            i=0
        elif (i < 19):
            i=1
        else:
            i=2
        new_age.append(i)
    return new_age

@app.route('/predict', methods=['POST'])
def predict():
    # Handle form submission and use the ML model
    age = request.form.get(('age'))
    famsize = request.form.get(('famsize'))
    Fedu = request.form.get(('Fedu'))
    Medu = request.form.get(('Medu'))
    Fjob = request.form.get(('Fjob'))
    Mjob = request.form.get(('Mjob'))
    traveltime = request.form.get(('traveltime'))
    studytime = request.form.get(('studytime'))
    failures = request.form.get(('failures'))
    paid = request.form.get(('paid'))
    nursery = request.form.get(('nursery'))
    internet = request.form.get(('internet'))
    goout = request.form.get(('goout'))
    Dalc = request.form.get(('Dalc'))
    ab = request.form.get(('age1'))

    # Perform prediction using the loaded ML model
    # Replace this with your actual prediction logic
    i1 = int(age)
    i2 = int(famsize)
    i3 = int(Fedu)
    i4 = int(Medu)
    i5 = int(Fjob)
    i6 = int(Mjob)
    i7 = int(traveltime)
    i8 = int(studytime)
    i9 = int(failures)
    i10 = int(paid)
    i11 = int(nursery)
    i12 = int(internet)
    i13 = int(goout)
    i14 = int(Dalc)
    i15 = int(ab)
    print(type(i15))
    features = np.array([[i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11,i12,i13,i14,i15]])
    print(features)
    prediction = model.predict(features)
    result_label = "FAIL" if prediction[0] == 0 else "PASS"
    # Render the result.html template with the prediction result
   
    return render_template('result.html', result=result_label)

if __name__ == '__main__':
    app.run(debug=True)
