import pandas as pd

# Load both CSVs without any datetime parsing
weather_df = pd.read_csv("hydro_predictor/hydro_predictor_data/seattle_hourly_weather_jan24_mar25.csv")
hydro_df = pd.read_csv("hydro_predictor/hydro_data/seattle_hydro_jan24_mar25.csv")

# Confirm they have the same number of rows
if len(weather_df) != len(hydro_df):
    raise ValueError(f"Mismatch in row counts: weather = {len(weather_df)}, hydro = {len(hydro_df)}")

# Combine them side by side
merged_df = pd.concat([weather_df, hydro_df], axis=1)

# Save the merged result
merged_df.to_csv("merged_hydro_weather_clean.csv", index=False)

print("✅ Merged successfully, row-by-row. Saved as 'merged_hydro_weather_clean.csv'")
