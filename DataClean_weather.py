import numpy as np
import pandas as pd

a = pd.read_csv('weather_messy.csv')
a.columns = a.columns.str.strip().str.lower()
print(a.shape)

# duplicates: exact rows, then repeated IDs
a = a.drop_duplicates().drop_duplicates(subset='record_id', keep='first')

# city: trim, fix aliases
b = {'bombay': 'Mumbai', 'bangalore': 'Bengaluru', 'calcutta': 'Kolkata',
     'madras': 'Chennai', 'new delhi': 'Delhi'}
a['city'] = a['city'].astype(str).str.strip().str.lower()
a['city'] = a['city'].replace(b).str.title()

# condition: trim and title case, blanks become Unknown
a['condition'] = a['condition'].fillna('').astype(str).str.strip().str.title()
a['condition'] = a['condition'].replace(['', 'Nan', 'N/A', '-'], 'Unknown')

# date: mixed formats, day first
a['date'] = pd.to_datetime(a['date'], format='mixed', dayfirst=True, errors='coerce')
a = a.dropna(subset=['date'])

# numbers: pull out digits, drop units
c = ['temp', 'humidity', 'pressure', 'wind_speed', 'rainfall']
for i in c:
    a[i] = pd.to_numeric(a[i].astype(str).str.extract(r'(-?\d+\.?\d*)')[0], errors='coerce')

# valid ranges, anything outside becomes NaN
r = {'temp': (-5, 50), 'humidity': (0, 100), 'pressure': (880, 1050),
     'wind_speed': (0, 150), 'rainfall': (0, 500)}
for i, (l, h) in r.items():
    a[i] = a[i].where(a[i].between(l, h))

# fill gaps with each city's median
for i in c:
    a[i] = a[i].fillna(a.groupby('city')[i].transform('median')).round(1)

a = a.sort_values(['city', 'date']).reset_index(drop=True)
a.to_csv('cleaned_weather.csv', index=False)
print(a.shape)
print(a.isna().sum().sum(), a['city'].unique())
