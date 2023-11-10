from flask import Flask, request, jsonify, render_template
import pickle 
import numpy as np 

app = Flask(__name__)
model = pickle.load(open('nbclassifier.pkl', 'rb'))
scaler = pickle.load(open('scaler.pickle', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    pre_final_features = [np.array(int_features)]
    final_features = scaler.transform(pre_final_features)
    prediction = model.predict(final_features)    
    if (prediction == 1):
        output = "True"
    elif(prediction == 0):
        output = "False"
    else:
        output = "Not sure"

    return render_template('index.html', prediction='This user is going to buy a product displayed on a social media advertisement **Result is:  {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
