import pickle
import numpy as np

# Load the trained regression model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict(data):
    try:
        bmi = float(data['bmi'])
        input_array = np.array([[bmi]])  # Ensure 2D input
        prediction = model.predict(input_array)
        return round(float(prediction[0]), 2)  # Return prediction as float
    except Exception as e:
        return f"Error in prediction: {str(e)}"