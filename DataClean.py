import numpy as np
import pandas as pd

# Load the messy CSV dataset
df = pd.read_csv('customer.csv')
print (df.head(10))
# 1. Remove duplicate customer IDs
df = df.drop_duplicates(subset=['CustomerID'], keep='first')

# 2. Clean Name column (Strip whitespace & Title case)
df['Name'] = df['Name'].astype(str).str.strip().str.title()

# 3. Clean & Standardize Gender
df['Gender'] = df['Gender'].astype(str).str.strip().str.upper()
gender_map = {
    'MALE': 'Male',
    'M': 'Male',
    'FEMALE': 'Female',
    'F': 'Female',
}
df['Gender'] = df['Gender'].map(gender_map).fillna('Unknown')

# 4. Clean Annual_Income (Strip $, commas, and handle negative values/NaNs)
df['Annual_Income'] = (
    df['Annual_Income']
    .astype(str)
    .str.replace('$', '', regex=False)
    .str.replace(',', '', regex=False)
    .replace('nan', np.nan)
)
df['Annual_Income'] = pd.to_numeric(df['Annual_Income'], errors='coerce')
df.loc[df['Annual_Income'] < 0, 'Annual_Income'] = np.nan

# Impute missing income with median
median_income = df['Annual_Income'].median()
df['Annual_Income'] = df['Annual_Income'].fillna(median_income)

# 5. Clean Age column & handle unrealistic outliers (keep between 18 and 100)
df.loc[(df['Age'] < 18) | (df['Age'] > 100), 'Age'] = np.nan
median_age = df['Age'].median()
df['Age'] = df['Age'].fillna(median_age).astype(int)

# 6. Parse and Standardize Signup_Date into datetime (YYYY-MM-DD)
df['Signup_Date'] = pd.to_datetime(df['Signup_Date'], errors='coerce')

# 7. Clean State column (Strip whitespace & Uppercase)
df['State'] = df['State'].astype(str).str.strip().str.upper()

# Export cleaned dataset
df.to_csv('cleaned_customer.csv', index=False)