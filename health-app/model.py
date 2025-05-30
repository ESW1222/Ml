import pickle
import numpy as np

# Load the trained model from the file only once when this file runs
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

def predict(data):
    # Get the BMI value from the input dictionary
    bmi = data.get('bmi')
    
    # If BMI is missing, show an error
    if bmi is None:
        raise ValueError("Please provide a BMI value.")
    
    # Convert BMI into the format the model expects (2D array)
    input_for_model = np.array([[bmi]])
    
    # Use the loaded model to make a prediction
    prediction = model.predict(input_for_model)
    
    # Return the prediction as a simple number (float)
    return float(prediction[0])