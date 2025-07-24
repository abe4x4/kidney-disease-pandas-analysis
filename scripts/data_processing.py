import pandas as pd

# Load the dataset
def load_data(filepath):
    return pd.read_csv(filepath)

# Clean the dataset (implement according to your needs)
def clean_data(df):
    df = df.dropna()  # Example: drop rows with missing values
    return df

# Example usage
if __name__ == '__main__':
    df = load_data('data/kidney_disease.csv')
    df_cleaned = clean_data(df)
    print(df_cleaned.head())