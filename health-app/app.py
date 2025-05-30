from flask import Flask, request, jsonify
from model import predict  # Make sure model.py exists and has a `predict` function

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Health Charges Prediction API!"

@app.route('/predict', methods=['POST'])
def predict_route():
    data = request.get_json()
    if not data or 'bmi' not in data:
        return jsonify({'error': 'Please provide BMI in the request JSON body.'}), 400
    try:
        bmi_value = float(data['bmi'])
        result = predict({'bmi': bmi_value})
        return jsonify({'bmi': bmi_value, 'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)