
import pandas as pd
import numpy as np

# Load the transformed data
df = pd.read_csv('data/processed/transformed_kidney.csv')

# --- GroupBy Operations ---

# 1. Average blood pressure by age group
avg_bp_by_age = df.groupby('age_group')['bp_normalized'].mean().reset_index()
print("Average Blood Pressure by Age Group:")
print(avg_bp_by_age)

# 2. Count of patients by classification within each age group
classification_counts = df.groupby(['age_group', 'classification']).size().unstack(fill_value=0)
print("
Patient Counts by Classification and Age Group:")
print(classification_counts)

# 3. Aggregating multiple metrics
# Calculate mean and standard deviation for 'bgr' and 'sc' for each classification
agg_metrics = df.groupby('classification').agg({
    'bgr': ['mean', 'std'],
    'sc': ['mean', 'std']
}).reset_index()

# Flatten the multi-level column index
agg_metrics.columns = ['_'.join(col).strip() for col in agg_metrics.columns.values]
print("
Aggregated Metrics (BGR and SC) by Classification:")
print(agg_metrics)

# 4. Applying a custom function
# Calculate the range of blood glucose for each age group
def glucose_range(series):
    return series.max() - series.min()

glucose_range_by_age = df.groupby('age_group')['bgr'].apply(glucose_range).reset_index(name='bgr_range')
print("
Glucose Range by Age Group:")
print(glucose_range_by_age)

# 5. Filtering groups
# Show only age groups where the average blood pressure is above the overall average
overall_avg_bp = df['bp_normalized'].mean()
high_bp_groups = df.groupby('age_group').filter(lambda x: x['bp_normalized'].mean() > overall_avg_bp)
print(f"
Groups with Average BP > {overall_avg_bp:.2f}:")
# To see the effect, let's show the average BP for these filtered groups
print(high_bp_groups.groupby('age_group')['bp_normalized'].mean())

# --- Save results to a log file for inspection ---
with open("reports/analysis_logs/a06_groupby_analysis.txt", "w") as f:
    f.write("Average Blood Pressure by Age Group:
")
    f.write(str(avg_bp_by_age))
    f.write("

Patient Counts by Classification and Age Group:
")
    f.write(str(classification_counts))
    f.write("

Aggregated Metrics (BGR and SC) by Classification:
")
    f.write(str(agg_metrics))
    f.write("

Glucose Range by Age Group:
")
    f.write(str(glucose_range_by_age))
    f.write(f"

Groups with Average BP > {overall_avg_bp:.2f}:
")
    f.write(str(high_bp_groups.groupby('age_group')['bp_normalized'].mean()))

print("
GroupBy analysis complete. Results saved to 'reports/analysis_logs/a06_groupby_analysis.txt'")
