"""
SECTION 1: Data Import/Export
- Load kidney disease dataset
- Demonstrate file I/O operations
"""
import pandas as pd
import os

def load_kidney_data():
    """Load and prepare kidney disease data with file operations"""
    print("\n=== SECTION 1: Data Import/Export ===")
    
    # Create required directories
    os.makedirs('data', exist_ok=True)
    os.makedirs('reports/analysis_logs', exist_ok=True)

    # Sample data (replace with actual CSV loading)
    data = {
        'age': [48, 62, 58, None, 45],
        'bp': [80, 90, 70, None, 110],
        'sg': [1.02, 1.01, None, 1.01, 1.02],
        'classification': ['ckd', 'ckd', 'notckd', None, 'ckd']
    }
    df = pd.DataFrame(data)
    
    # File operations (core Section 1 skill)
    df.to_csv('data/raw_kidney.csv', index=False)
    print("Data saved to data/raw_kidney.csv")
    
    return df

if __name__ == "__main__":
    df = load_kidney_data()
    print("\nFirst 5 records:")
    print(df.head())