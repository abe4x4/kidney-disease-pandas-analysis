"""
SECTION 2: Data Exploration
- Basic dataset statistics
- Missing value analysis
- Data type inspection
"""
import pandas as pd
import os
from a01_data_import import load_kidney_data 
def explore_data(df):
    """Perform comprehensive data exploration"""
    print("\n=== SECTION 2: Data Exploration ===")
    
    # 1. Basic info
    print("\n1. Dataset Structure:")
    print(f"Shape: {df.shape}")
    print(f"\nColumns: {df.columns.tolist()}")
    
    # 2. Data types
    print("\n2. Data Types:")
    print(df.dtypes)
    
    # 3. Missing values
    print("\n3. Missing Values:")
    print(df.isnull().sum())
    
    # 4. Save findings
    with open('reports/analysis_logs/initial_findings.txt', 'w') as f:
        f.write(f"=== Exploration Report ===\n")
        f.write(f"Shape: {df.shape}\n\n")
        f.write(f"Missing Values:\n{df.isnull().sum()}\n\n")
        f.write(f"Data Types:\n{df.dtypes}")

if __name__ == "__main__":
    print("Starting data exploration...")
    try:
        df = load_kidney_data()
        explore_data(df)
        print("\nExploration complete! Results saved to reports/analysis_logs/")
    except Exception as e:
        print(f"\nError during exploration: {str(e)}")