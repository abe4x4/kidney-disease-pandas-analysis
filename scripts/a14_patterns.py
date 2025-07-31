
import pandas as pd

# Load the cleaned data
df = pd.read_csv('data/processed/cleaned_kidney.csv')

# --- Method Chaining ---
def preprocess_data(df):
    return (
        df.copy()
        .assign(
            bp_to_age_ratio=df['bp'] / df['age'],
            is_hypertensive=lambda x: x['bp'] > 80
        )
        .query('is_hypertensive')
        .sort_values(by='bp_to_age_ratio', ascending=False)
    )

processed_df = preprocess_data(df)
print("Method chaining example:")
print(processed_df.head())

# --- String Accessor ---
df['classification_upper'] = df['classification'].str.upper()
print("\nString accessor example:")
print(df[['classification', 'classification_upper']].head())

# --- Datetime Accessor ---
df['record_date'] = pd.to_datetime(df['record_date'])
df['day_of_week'] = df['record_date'].dt.day_name()
print("\nDatetime accessor example:")
print(df[['record_date', 'day_of_week']].head())
