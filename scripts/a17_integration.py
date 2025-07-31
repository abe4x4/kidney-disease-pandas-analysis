
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the preprocessed data
X = pd.read_csv('data/processed/processed_for_ml.csv')
y = pd.read_csv('data/processed/cleaned_kidney.csv')['classification']

# --- Integration with NumPy ---
# Convert DataFrame to NumPy array for numerical computations
X_np = X.to_numpy()
print("Shape of the NumPy array:", X_np.shape)

# --- Integration with Scikit-learn ---
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy:.4f}")
