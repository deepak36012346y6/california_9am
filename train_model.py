from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import joblib

# Load California Housing dataset
housing = fetch_california_housing()

# Create DataFrame
X = pd.DataFrame(
    housing.data,
    columns=housing.feature_names
)

y = housing.target

# Create the machine learning model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train the model
print("Training model...")
model.fit(X, y)

# Save the trained model
joblib.dump(model, "california.joblib")

print("Model trained successfully!")
print("california.joblib created successfully!")
