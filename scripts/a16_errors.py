
import pandas as pd

# --- Handling KeyError ---
try:
    df = pd.read_csv('data/processed/cleaned_kidney.csv')
    print(df['non_existent_column'])
except KeyError as e:
    print(f"Caught a KeyError: {e}")

# --- Handling SettingWithCopyWarning ---
# This warning can be subtle. The best practice is to use .loc for assignment.
df_slice = df[df['age'] > 70]

# This might raise a SettingWithCopyWarning
# df_slice['age_plus_one'] = df_slice['age'] + 1

# The correct way to avoid the warning is to use .copy()
df_slice = df[df['age'] > 70].copy()
df_slice['age_plus_one'] = df_slice['age'] + 1
print("\nSuccessfully avoided SettingWithCopyWarning by using .copy()")

# --- Handling DtypeWarning ---
# This can happen with mixed types in a column. Explicitly set dtypes.
try:
    # Create a dummy file with mixed types
    with open('data/mixed_types.csv', 'w') as f:
        f.write("a,b\n1,2\nhello,4\n3,world")
    
    # This will likely raise a DtypeWarning
    df_mixed = pd.read_csv('data/mixed_types.csv')
    print(df_mixed.dtypes)

    # The correct way is to specify dtypes
    df_mixed_fixed = pd.read_csv('data/mixed_types.csv', dtype={'a': str, 'b': str})
    print("\nSuccessfully avoided DtypeWarning by specifying dtypes:")
    print(df_mixed_fixed.dtypes)

except Exception as e:
    print(f"An error occurred: {e}")
