import pandas as pd

# Load CSVs 
df_hydro = pd.read_csv('hydro_predictor/hydro_weather_data/seattle_hydro_weather_jan24_mar25.csv')
df_demand = pd.read_csv('hydro_predictor/hydro_demand/demand_jan24_mar25.csv', usecols=['Timestamp (Hour Ending)', 'Demand (MWh)'])

# Clean function handles both PST and PDT
def clean_timestamp_column(series):
    cleaned = (
        series.str.replace(' a.m.', ' AM', regex=False)
              .str.replace(' p.m.', ' PM', regex=False)
              .str.replace(' PST', '', regex=False)
              .str.replace(' PDT', '', regex=False)
    )
    return pd.to_datetime(cleaned, format='%m/%d/%Y %I %p')


# Apply cleaned timestamp function
df_hydro['timestamp'] = clean_timestamp_column(df_hydro['Timestamp (Hour Ending)'])
df_demand['timestamp'] = clean_timestamp_column(df_demand['Timestamp (Hour Ending)'])

# Merge
df_merged = pd.merge(df_hydro, df_demand[['timestamp', 'Demand (MWh)']], on='timestamp', how='inner')

# Save result
df_merged.to_csv('merged_hydro_demand.csv', index=False)
print("✅ Merge complete. Rows:", len(df_merged))