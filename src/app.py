from flask import Flask, render_template, request, jsonify,send_file
import numpy as np
import joblib

app = Flask(__name__)

# Load the trained SVM model
clf = joblib.load('Cell_quality/models/trained_model.pkl')

# Define a route for the home page
@app.route('/')
def home():
    return send_file(r"C:\vs code\ML\SVM\Cell_quality\templates\index.html")

# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the request
    data = request.json
    
    # Extract features from the data
    clump = data['clump']
    uniformity = data['uniformity']
    shape = data['shape']
    adhesion = data['adhesion']
    epiSize = data['epiSize']
    bareNuc = data['bareNuc']
    chromatin = data['chromatin']
    normNucl = data['normNucl']
    mitoses = data['mitoses']
    
    # Make prediction
    prediction = clf.predict(np.array([[clump, uniformity, shape, adhesion, epiSize, bareNuc, chromatin, normNucl, mitoses]]))
    
    # Convert prediction to string (assuming 2 is benign and 4 is malignant)
    prediction_str = 'Benign' if prediction == 2 else 'Malignant'
    
    return jsonify({'prediction': prediction_str})

if __name__ == '__main__':
    app.run(debug=True)
