
import pandas as pd
import time

# Load the cleaned data
df = pd.read_csv('data/processed/cleaned_kidney.csv')

# --- Performance of apply vs. vectorized operations ---

# Using apply (slower)
start_time = time.time()
df['bp_category_apply'] = df['bp'].apply(lambda x: 'high' if x > 80 else 'normal')
end_time = time.time()
print(f"Time taken with apply: {end_time - start_time:.4f} seconds")

# Using vectorized operation (faster)
start_time = time.time()
df['bp_category_vectorized'] = 'normal'
df.loc[df['bp'] > 80, 'bp_category_vectorized'] = 'high'
end_time = time.time()
print(f"Time taken with vectorized operation: {end_time - start_time:.4f} seconds")

# --- Performance of different file formats ---

# Parquet (generally faster and more memory efficient)
start_time = time.time()
df.to_parquet('data/processed/kidney.parquet')
pd.read_parquet('data/processed/kidney.parquet')
end_time = time.time()
print(f"Time taken for Parquet I/O: {end_time - start_time:.4f} seconds")

# CSV
start_time = time.time()
df.to_csv('data/processed/kidney_temp.csv')
pd.read_csv('data/processed/kidney_temp.csv')
end_time = time.time()
print(f"Time taken for CSV I/O: {end_time - start_time:.4f} seconds")
