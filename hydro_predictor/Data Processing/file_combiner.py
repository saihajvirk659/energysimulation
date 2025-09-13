import pandas as pd

# Standard column names
columns = ['BA Code', 'Timestamp (Hour Ending)', 'Demand (MWh)']

def load_clean_csv(path):
    # Load file with auto-detected header
    df = pd.read_csv(path)

    # Drop any rows where header was accidentally repeated
    df = df[df['BA Code'] != 'BA Code']

    # Standardize columns (in case some files have slightly different formatting)
    df = df.rename(columns=lambda x: x.strip())  # Trim whitespace
    df = df[columns]  # Reorder or select correct columns

    return df

# List all CSVs
months = [
    'demand_jan24.csv', 'demand_feb24.csv', 'demand_mar24.csv',
    'demand_apr24.csv', 'demand_may24.csv', 'demand_jun24.csv',
    'demand_jul24.csv', 'demand_aug24.csv', 'demand_sep24.csv',
    'demand_oct24.csv', 'demand_nov24.csv', 'demand_dec24.csv',
    'demand_jan25.csv', 'demand_feb25.csv', 'demand_mar25.csv'
]

# Load and combine
dfs = [load_clean_csv(f"hydro_predictor/hydro_demand/{m}") for m in months]
combined = pd.concat(dfs, ignore_index=True)

# Save
combined.to_csv('seattle_hydro_combined.csv', index=False)
print(f"✅ Combined file created successfully with {len(combined)} rows.")
