"""
Section 1: Data Import/Export
- Load kidney disease dataset
- Demonstrate DataFrame creation
- Basic file I/O operations
"""

import pandas as pd
import os

def load_kidney_data():
    """Load and display kidney disease dataset"""
    print("=== Loading Kidney Disease Dataset ===")
    
    # Create data directory if needed
    os.makedirs('data', exist_ok=True)
    
    # Sample data creation (replace with actual CSV load)
    data = {
        'age': [48, 62, 58, None, 45],
        'bp': [80, 90, 70, None, 110],
        'sg': [1.02, 1.01, None, 1.01, 1.02],
        'classification': ['ckd', 'ckd', 'notckd', None, 'ckd']
    }
    df = pd.DataFrame(data)
    
    # Save to CSV for demonstration
    df.to_csv('data/raw_kidney.csv', index=False)
    print("Sample kidney data created at data/raw_kidney.csv")
    
    return df

if __name__ == "__main__":
    kidney_df = load_kidney_data()
    print("\nFirst 5 records:")
    print(kidney_df.head())