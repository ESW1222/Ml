import json
from app import app  # Make sure `app = Flask(__name__)` is defined in your app.py

# Test the home endpoint
def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Health Charges Prediction API!" in response.data

# Test the predict endpoint with a valid BMI
def test_predict_valid_bmi():
    tester = app.test_client()
    response = tester.post(
        '/predict',
        data=json.dumps({'bmi': 26.5}),
        content_type='application/json'
    )
    assert response.status_code == 200
    data = response.get_json()
    assert 'prediction' in data
    assert isinstance(data['prediction'], float)

# Test the predict endpoint with missing BMI
def test_predict_missing_bmi():
    tester = app.test_client()
    response = tester.post(
        '/predict',
        data=json.dumps({}),
        content_type='application/json'
    )
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data

# Test the predict endpoint with invalid BMI type
def test_predict_invalid_bmi():
    tester = app.test_client()
    response = tester.post(
        '/predict',
        data=json.dumps({'bmi': "invalid"}),
        content_type='application/json'
    )
    assert response.status_code == 500
    data = response.get_json()
    assert 'error' in data