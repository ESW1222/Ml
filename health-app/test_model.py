import pickle
import numpy as np

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

bmi = 30.0
prediction = model.predict(np.array([[bmi]]))

print(f"Predicted charges for BMI {bmi}: {prediction[0]:.2f}")
