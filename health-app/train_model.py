import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

data = pd.read_csv('health_data.csv')
X = data[['bmi']]
y = data['charges']

model = LinearRegression()
model.fit(X, y)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as model.pkl")
