
import pandas as pd
import numpy as np

# Load the merged dataset
df = pd.read_csv('data/processed/merged_kidney_data.csv')

# --- Time Series Preparation ---
# The dataset does not have a timestamp, so we will create a synthetic one.
# Let's assume these patient records were created over a period of time.
start_date = "2022-01-01"
end_date = "2022-12-31"

# Create a date range and assign it to the dataframe
dates = pd.to_datetime(np.linspace(pd.to_datetime(start_date).value, pd.to_datetime(end_date).value, len(df)))
df['record_date'] = dates

# Set the date as the index
df.set_index('record_date', inplace=True)

print("Time series data prepared with a synthetic 'record_date'.")

# --- Time Series Operations ---

# 1. Resampling: Aggregate data by month
# Let's count the number of new cases and the average blood pressure per month.
monthly_summary = df.resample('M').agg({
    'id': 'count', 
    'bp': 'mean'
}).rename(columns={'id': 'patient_count', 'bp': 'avg_bp'})

print("\nMonthly Summary (Patient Count and Average BP):")
print(monthly_summary)

# 2. Rolling Window: Calculate a 30-day rolling average of serum creatinine
# This helps to smooth out short-term fluctuations and identify trends.
df_sorted = df.sort_index() # Ensure data is sorted by date for rolling calculations
rolling_avg_sc = df_sorted['sc'].rolling(window='30D').mean()

print("\nLast 5 values of 30-Day Rolling Average of Serum Creatinine:")
print(rolling_avg_sc.tail())

# 3. Shifting: Compare current blood glucose with the previous record
# This is useful for tracking progression or changes over time.
df_sorted['bgr_previous'] = df_sorted['bgr'].shift(1)
df_sorted['bgr_change'] = df_sorted['bgr'] - df_sorted['bgr_previous']

print("\nBlood Glucose Change from Previous Record (last 5 records):")
print(df_sorted[['bgr', 'bgr_previous', 'bgr_change']].tail())

# --- Save results to a log file for inspection ---
with open("reports/analysis_logs/a09_timeseries_analysis.txt", "w") as f:
    f.write("Monthly Summary (Patient Count and Average BP):\n")
    f.write(str(monthly_summary))
    f.write("\n\nLast 5 values of 30-Day Rolling Average of Serum Creatinine:\n")
    f.write(str(rolling_avg_sc.tail()))
    f.write("\n\nBlood Glucose Change from Previous Record (last 5 records):\n")
    f.write(str(df_sorted[['bgr', 'bgr_previous', 'bgr_change']].tail()))

print("\nTime series analysis complete. Results saved to 'reports/analysis_logs/a09_timeseries_analysis.txt'")
