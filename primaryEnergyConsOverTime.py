import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Load data
file_path = "./datasets/primary-energy-cons.csv"  
df = pd.read_csv(file_path)

# Optional: clean column names (strip whitespace)
df.columns = df.columns.str.strip()

# Select countries to visualize
selected_countries = ["Afghanistan", "India", "United States"]

# Filter dataset
filtered_df = df[df["Entity"].isin(selected_countries)]

# Create interactive line chart
fig = px.line(
    filtered_df,
    x="Year",
    y="Primary energy consumption (TWh)",
    color="Entity",
    title="Primary Energy Consumption Over Time (TWh)",
    labels={"Primary energy consumption (TWh)": "Energy Consumption (TWh)"}
)

# Show the chart
fig.show()