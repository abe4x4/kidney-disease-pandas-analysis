
import pandas as pd

# --- Load Datasets ---
# Load the main cleaned dataset
df_kidney = pd.read_csv('data/processed/transformed_kidney.csv')

# Create a dummy demographics dataset
# In a real scenario, this might come from a separate hospital registration system
demographics_data = {
    'id': df_kidney['id'],
    'gender': ['Male', 'Female'] * (len(df_kidney) // 2) + ['Male'] * (len(df_kidney) % 2),
    'city': ['New York', 'Los Angeles', 'Chicago', 'Houston'] * (len(df_kidney) // 4) + ['New York'] * (len(df_kidney) % 4)
}
df_demographics = pd.DataFrame(demographics_data)

# Create a dummy lab results dataset
# This could represent a different set of tests from another lab system
lab_data = {
    'id': df_kidney['id'].sample(frac=0.8, random_state=42),  # Not all patients may have these tests
    'hemoglobin_level': (pd.Series(df_kidney['hemo'] * 0.95).round(2)), # Simulate a slightly different reading
    'serum_creatinine_clearance': (pd.Series(df_kidney['sc'] * 10).round(2)) # Different unit or scale
}
df_lab = pd.DataFrame(lab_data)


# --- Merging Operations ---

# 1. Inner Join: Combine kidney data with demographics
# This keeps only the patients present in both dataframes (which is all of them in this case)
df_merged_inner = pd.merge(df_kidney, df_demographics, on='id', how='inner')
print("Shape after inner join with demographics:", df_merged_inner.shape)

# 2. Left Join: Add new lab results to the main dataframe
# This keeps all patients from the main dataframe, filling missing lab values with NaN
df_merged_left = pd.merge(df_merged_inner, df_lab, on='id', how='left')
print("Shape after left join with lab data:", df_merged_left.shape)

# Verify that NaNs were introduced for patients not in the lab dataset
print(f"NaNs in hemoglobin_level after left join: {df_merged_left['hemoglobin_level'].isnull().sum()}")

# 3. Outer Join: Combine two hypothetical patient lists
# This would keep all patients from both lists, regardless of whether they are in the other
# Let's create another small list of patients for this example
additional_patients_data = {
    'id': [999, 1000],  # New patient IDs not in the original dataset
    'contact_person': ['John Doe', 'Jane Smith']
}
df_additional_patients = pd.DataFrame(additional_patients_data)

df_outer_join = pd.merge(df_merged_left, df_additional_patients, on='id', how='outer')
print("
Shape after outer join with additional patients:", df_outer_join.shape)
print("Tail of the outer-joined dataframe to see new patients:")
print(df_outer_join.tail())

# --- Save the primary merged file ---
df_merged_left.to_csv('data/processed/merged_kidney_data.csv', index=False)

print("
Merging complete. Primary merged data saved to 'data/processed/merged_kidney_data.csv'")
