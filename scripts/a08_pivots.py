
import pandas as pd

# Load the merged dataset
df = pd.read_csv('data/processed/merged_kidney_data.csv')

# --- Pivot Table Operations ---

# 1. Basic Pivot Table: Average blood pressure by age group and classification
# This gives a clear matrix showing how average blood pressure varies across these two dimensions.
pivot_bp = df.pivot_table(
    values='bp', 
    index='age_group', 
    columns='classification', 
    aggfunc='mean'
)
pivot_bp.fillna(0, inplace=True) # Fill non-existent combinations with 0
print("Pivot Table: Average Blood Pressure by Age Group and Classification")
print(pivot_bp)

# 2. Advanced Pivot Table: Multiple aggregations
# Let's analyze blood glucose ('bgr') and serum creatinine ('sc') levels
# across age groups and classifications, calculating both mean and max.
pivot_advanced = df.pivot_table(
    values=['bgr', 'sc'],
    index=['city', 'age_group'],
    columns='classification',
    aggfunc={'bgr': ['mean', 'max'], 'sc': 'mean'}
)
pivot_advanced.fillna(0, inplace=True)
print("
Advanced Pivot Table: BGR (Mean/Max) and SC (Mean) by City, Age Group, and Classification")
print(pivot_advanced)

# 3. Pivot with Margins: Add totals for rows and columns
# This is useful for seeing both individual segment data and overall totals in one view.
pivot_with_margins = df.pivot_table(
    values='id', 
    index='age_group', 
    columns='classification', 
    aggfunc='count', 
    margins=True, # Add row and column totals
    margins_name='Total Count' # Custom name for the margins
)
pivot_with_margins.fillna(0, inplace=True)
print("
Pivot Table with Margins: Patient Count by Age Group and Classification")
print(pivot_with_margins)

# --- Save results to a log file for inspection ---
with open("reports/analysis_logs/a08_pivots_analysis.txt", "w") as f:
    f.write("Pivot Table: Average Blood Pressure by Age Group and Classification\n")
    f.write(str(pivot_bp))
    f.write("\n\nAdvanced Pivot Table: BGR (Mean/Max) and SC (Mean) by City, Age Group, and Classification\n")
    f.write(str(pivot_advanced))
    f.write("\n\nPivot Table with Margins: Patient Count by Age Group and Classification\n")
    f.write(str(pivot_with_margins))

print("\nPivot table analysis complete. Results saved to 'reports/analysis_logs/a08_pivots_analysis.txt'")
