
import pandas as pd

# Load the main dataset
df = pd.read_csv('data/processed/merged_kidney_data.csv')

# --- Advanced Features ---

# 1. Using Categorical Data More Deeply
# Convert 'classification' and 'age_group' to ordered categorical types
# This can improve performance and allows for logical sorting.
df['classification'] = pd.Categorical(df['classification'], categories=['notckd', 'ckd'], ordered=True)
df['age_group'] = pd.Categorical(df['age_group'], categories=['<30', '30-45', '46-60', '60+'], ordered=True)

print("Converted 'classification' and 'age_group' to ordered categorical types.")
print("Sorted by age group and classification:")
print(df.sort_values(by=['age_group', 'classification']).head())

# 2. Multi-level Indexing
# Create a multi-level index on 'city' and 'age_group' to facilitate more complex queries.
df_multi_index = df.set_index(['city', 'age_group'])
print("\nDataFrame with Multi-level Index (City and Age Group):")
print(df_multi_index.head())

# Example: Select all patients from 'New York' in the '46-60' age group
print("\nQuerying with multi-level index (New York, 46-60):")
print(df_multi_index.loc[pd.IndexSlice['New York', '46-60'], :])

# 3. Using `pipe` for cleaner data processing workflows
# Define a function to calculate a new metric and another to log the output.

def calculate_bgr_to_sc_ratio(dataframe):
    """Calculates the ratio of blood glucose to serum creatinine."""
    dataframe['bgr_sc_ratio'] = dataframe['bgr'] / dataframe['sc']
    return dataframe

def log_head(dataframe, n=5):
    """Logs the first n rows of the dataframe."""
    print(f"\nLogging top {n} rows after pipe operations:")
    print(dataframe.head(n))
    return dataframe

# Chain these operations using `pipe`
processed_df = (
    df.copy()
    .pipe(calculate_bgr_to_sc_ratio)
    .pipe(log_head)
)

# 4. Exploding a list-like column
# Let's create a synthetic column where each patient has a list of medications.
medications = [['Lisinopril', 'Metformin'], ['Amlodipine'], ['Metformin', 'Atorvastatin', 'Lisinopril']]
df['medications'] = medications * (len(df) // 3) + medications[:len(df) % 3]

# Use `explode` to transform each medication into its own row
df_exploded = df.explode('medications')
print("\nDataFrame after exploding the 'medications' column (first 10 rows):")
print(df_exploded[['id', 'medications']].head(10))

# --- Save results to a log file for inspection ---
with open("reports/analysis_logs/a10_advanced_analysis.txt", "w") as f:
    f.write("Sorted by age group and classification:\n")
    f.write(str(df.sort_values(by=['age_group', 'classification']).head()))
    f.write("\n\nQuerying with multi-level index (New York, 46-60):\n")
    f.write(str(df_multi_index.loc[pd.IndexSlice['New York', '46-60'], :]))
    f.write("\n\nDataFrame after exploding the 'medications' column (first 10 rows):\n")
    f.write(str(df_exploded[['id', 'medications']].head(10)))

print("\nAdvanced analysis complete. Results saved to 'reports/analysis_logs/a10_advanced_analysis.txt'")
