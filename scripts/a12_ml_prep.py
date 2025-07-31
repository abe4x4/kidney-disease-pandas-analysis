
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Load the cleaned data
df = pd.read_csv('data/processed/merged_kidney_data.csv')

# Separate features and target
X = df.drop('classification', axis=1)
y = df['classification']

# Identify categorical and numerical features
categorical_features = X.select_dtypes(include=['object', 'category']).columns
numerical_features = X.select_dtypes(include=['int64', 'float64']).columns

# Create preprocessing pipelines for numerical and categorical features
numerical_pipeline = Pipeline(steps=[
    ('scaler', StandardScaler())
])

categorical_pipeline = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Create a column transformer to apply different transformations to different columns
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_pipeline, numerical_features),
        ('cat', categorical_pipeline, categorical_features)
    ])

# Fit and transform the data
X_processed = preprocessor.fit_transform(X)

# Save the processed data
pd.DataFrame(X_processed).to_csv('data/processed/processed_for_ml.csv', index=False)

print("Data prepared for machine learning and saved to data/processed/processed_for_ml.csv")
