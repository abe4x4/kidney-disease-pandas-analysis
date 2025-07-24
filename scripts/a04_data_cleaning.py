"""
SECTION 4: Data Cleaning & Preprocessing
- Handle missing values in kidney dataset
- Remove duplicates
- Fix data types
"""
import pandas as pd
from a01_data_import import load_kidney_data  # Using a-prefix import
import os

def clean_data(df):
    """Clean kidney disease dataset with comprehensive preprocessing"""
    print("\n=== SECTION 4: Data Cleaning ===")
    
    # 1. Handle missing values
    print("\n1. Handling missing values:")
    # Fill numeric columns with median (better for skewed medical data)
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    
    # Fill categorical with mode
    categorical_cols = df.select_dtypes(include=['object']).columns
    df[categorical_cols] = df[categorical_cols].fillna(df[categorical_cols].mode().iloc[0])
    
    # 2. Remove duplicates
    print("2. Removing duplicates...")
    initial_rows = len(df)
    df.drop_duplicates(inplace=True)
    print(f"Removed {initial_rows - len(df)} duplicate rows")
    
    # 3. Fix data types
    print("3. Fixing data types...")
    df['classification'] = df['classification'].astype('category')
    
    # Save cleaned data
    os.makedirs('data/processed', exist_ok=True)
    df.to_csv('data/processed/cleaned_kidney.csv', index=False)
    return df

if __name__ == "__main__":
    raw_data = load_kidney_data()
    cleaned_data = clean_data(raw_data)
    print("\nCleaned data summary:")
    print(cleaned_data.info())