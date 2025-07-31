
import pandas as pd

# Load the cleaned data
df = pd.read_csv('data/processed/cleaned_kidney.csv')

# --- Case Study 1: High-Risk CKD Patients ---
# Identify patients with CKD, high blood pressure, and high blood glucose
high_risk_ckd = df[
    (df['classification'] == 'ckd') &
    (df['bp'] > 80) &
    (df['bgr'] > 126)
]
print("Case Study 1: High-Risk CKD Patients")
print(high_risk_ckd[['age', 'bp', 'bgr', 'sc']])

# --- Case Study 2: Younger Patients with Kidney Disease ---
# Analyze kidney disease in patients under 40
young_patients_ckd = df[
    (df['classification'] == 'ckd') &
    (df['age'] < 40)
]
print("\nCase Study 2: Younger Patients with Kidney Disease")
print(young_patients_ckd[['age', 'bp', 'sg', 'al', 'su']])

# --- Case Study 3: Patients with Normal Vitals but CKD ---
# Find patients classified with CKD despite normal blood pressure and sugar
normal_vitals_ckd = df[
    (df['classification'] == 'ckd') &
    (df['bp'] <= 80) &
    (df['bgr'] <= 126)
]
print("\nCase Study 3: Patients with Normal Vitals but CKD")
print(normal_vitals_ckd[['age', 'hemo', 'pcv', 'rbcc']])
