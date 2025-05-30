from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return "Welcome to Health App!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    bmi = float(data['bmi'])
    prediction = model.predict(np.array([[bmi]]))
    return jsonify({'predicted_charges': prediction[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
