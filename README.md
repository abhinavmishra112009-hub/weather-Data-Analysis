# Weather Data Analytics – Data Cleaning Module

A Python-based data cleaning script that prepares raw daily weather observations for further analysis.

## Project Overview

`DataClean_weather.py` reads weather data from `weather_messy.csv`, cleans inconsistent records and values, and exports the processed data to `cleaned_weather.csv`.

The script uses **Python**, **pandas**, and **NumPy**.

## Features

- Reads the raw CSV file using pandas.
- Normalises column names by removing extra spaces and converting them to lowercase.
- Removes exact duplicate rows and keeps the first row for each repeated `record_id`.
- Standardises city names and maps historical aliases:
  - Bombay → Mumbai
  - Bangalore → Bengaluru
  - Calcutta → Kolkata
  - Madras → Chennai
  - New Delhi → Delhi
- Cleans weather-condition labels and replaces blank or placeholder values with `Unknown`.
- Parses mixed date formats using day-first interpretation.
- Removes rows with dates that cannot be parsed.
- Extracts numeric values from measurements containing units or symbols.
- Checks measurements against valid ranges.
- Fills missing numeric values using the median for the corresponding city.
- Sorts the cleaned records by city and date.
- Exports the cleaned dataset to a new CSV file.

## Requirements

- Python 3.9 or later
- pandas
- NumPy

Install the required libraries:

```bash
pip install pandas numpy
```

## Project Files

Keep the following files in the same folder:

```text
Weather-Data-Analysis/
├── DataClean_weather.py
├── weather_messy.csv
└── cleaned_weather.csv    # generated after running the script
```

## How to Run

1. Install Python and the required libraries.
2. Place `DataClean_weather.py` and `weather_messy.csv` in the same folder.
3. Open that folder in VS Code.
4. Open the VS Code terminal.
5. Run:

```bash
python DataClean_weather.py
```

After successful execution, the script creates `cleaned_weather.csv` in the same folder and prints the dataset shape, remaining missing-value count, and unique city names.

## Data Validation Ranges

Values outside these ranges are treated as missing before median imputation.

| Column | Minimum | Maximum | Unit |
|---|---:|---:|---|
| `temp` | -5 | 50 | °C |
| `humidity` | 0 | 100 | % |
| `pressure` | 880 | 1050 | hPa |
| `wind_speed` | 0 | 150 | km/h |
| `rainfall` | 0 | 500 | mm |

## Input Columns

The input CSV is expected to contain:

`record_id`, `date`, `city`, `temp`, `humidity`, `pressure`, `wind_speed`, `rainfall`, and `condition`.

## Output

The script generates **`cleaned_weather.csv`** with cleaned and standardised weather records. The output is sorted by city and date and is saved without an additional index column. The original input file is not overwritten.

## Important Notes

- The input CSV must be named `weather_messy.csv`.
- The input CSV must be in the same directory as the Python script.
- Date parsing uses day-first interpretation.
- Missing numeric measurements are filled using city-wise medians.
- If a city has no valid values for a numeric field, check the printed missing-value count after execution.
- This script covers data cleaning and preparation; exploratory analysis and visualisation are outside its current scope.

## GitHub Repository

`abhinavmishra112009-hub/weather-Data-Analysis`
