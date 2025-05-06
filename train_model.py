# train_model.py
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Example data
data = pd.DataFrame({
    'beds': [2, 3, 4, 5],
    'baths': [1, 2, 3, 4],
    'size': [1000, 1500, 2000, 2500],
    'zip_code': [12345, 12345, 67890, 67890],
    'price': [200000, 300000, 400000, 500000]
})

X = data[['beds', 'baths', 'size', 'zip_code']]
y = data['price']

model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, 'model.pkl')
