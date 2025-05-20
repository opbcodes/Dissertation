import pandas as pd
import plotly.express as px

# Load data
file_path = "./datasets/primary-energy-cons.csv"  
df = pd.read_csv(file_path)

# Optional: clean column names (strip whitespace)
# df.columns = df.columns.str.strip()

# Sort and compute year-over-year change
df_sorted = df.sort_values(by=["Entity", "Year"])
df_sorted["YoY Change"] = df_sorted.groupby("Entity")["Primary energy consumption (TWh)"].diff()

# Calculate volatility as standard deviation of YoY change
volatility_df = df_sorted.groupby("Entity")["YoY Change"].std().reset_index()
volatility_df.columns = ["Entity", "Volatility (Std Dev of YoY Change)"]

# Filter out aggregates and non-country entries
exclude_list = [
    "World", "Non-OECD (EIA)", "OECD (EIA)", "Non-OPEC (EIA)", "OPEC (EIA)",
    "Upper-middle-income countries", "Lower-middle-income countries",
    "High-income countries", "Low-income countries"
]
volatility_df = volatility_df[~volatility_df["Entity"].isin(exclude_list)]
volatility_df = volatility_df.dropna()

# Create the choropleth map
fig = px.choropleth(
    volatility_df,
    locations="Entity",
    locationmode="country names",
    color="Volatility (Std Dev of YoY Change)",
    hover_name="Entity",
    color_continuous_scale="Viridis",
    title="Volatility in Year-over-Year Energy Consumption by Country"
)

fig.update_layout(geo=dict(showframe=False, showcoastlines=False))
fig.show()