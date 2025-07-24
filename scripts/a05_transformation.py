"""
SECTION 5: Data Transformation
- Create new columns for kidney analysis
- Apply clinical transformations
- Sort/rank medical data
"""
import pandas as pd
import os
from a01_data_import import load_kidney_data  # Fixed import
from a04_data_cleaning import clean_data      # Import cleaning function

def transform_data(df):
    """Transform kidney disease data with clinical feature engineering"""
    print("\n=== SECTION 5: Data Transformation ===")
    
    # 1. Create clinically relevant age groups
    print("\n1. Creating CKD risk age categories...")
    bins = [0, 30, 45, 60, 100]
    labels = ['Low Risk', 'Moderate Risk', 'High Risk', 'Critical Risk']
    df['ckd_risk_age'] = pd.cut(df['age'], bins=bins, labels=labels)
    
    # 2. Normalize blood pressure (clinical z-score)
    print("2. Normalizing blood pressure...")
    df['bp_zscore'] = (df['bp'] - df['bp'].mean()) / df['bp'].std()
    
    # 3. Sort by clinical priority (age + BP)
    print("3. Sorting by clinical priority...")
    df.sort_values(['ckd_risk_age', 'bp'], 
                 ascending=[True, False], 
                 inplace=True)
    
    # Save transformed data
    os.makedirs('data/processed', exist_ok=True)
    df.to_csv('data/processed/transformed_kidney.csv', index=False)
    return df

if __name__ == "__main__":
    # Proper execution chain
    raw_data = load_kidney_data()         # From a01
    cleaned_data = clean_data(raw_data)   # From a04
    transformed_data = transform_data(cleaned_data)
    
    print("\nTransformed kidney data summary:")
    print("New columns:", list(transformed_data.columns))
    print("Risk categories:", transformed_data['ckd_risk_age'].unique())