# Y-axis shows % of total energy, not raw TWh. This makes it easier to see relative importance and shifts over time — e.g., how coal's share dropped while solar rose.

import matplotlib.pyplot as plt
import pandas as pd

# Load data
file_path = "./datasets/global-energy-substitution.csv"  
df = pd.read_csv(file_path)

# Drop irrelevant columns if they exist
df = df.drop(columns=["Entity", "Code"], errors="ignore")

# Drop rows with missing values
df = df.dropna()

# Convert 'Year' column to integer safely
df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")

# Convert all other columns to numeric
for col in df.columns:
    if col != "Year":
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Drop rows without valid years
df = df.dropna(subset=["Year"])

# Replace remaining NaNs with 0
df = df.fillna(0)

# Set Year as integer index
df["Year"] = df["Year"].astype(int)
df.set_index("Year", inplace=True)

# Ensure column names are strings
df.columns = df.columns.map(str)

# Convert values to percentage of total energy for each year
df_percent = df.div(df.sum(axis=1), axis=0) * 100

# Plot percentage stackplot
plt.figure(figsize=(12, 6))
plt.stackplot(df_percent.index, *[df_percent[col] for col in df_percent.columns], labels=df_percent.columns, alpha=0.8)

# Labels and formatting
plt.xlabel("Year")
plt.ylabel("Share of Global Energy Consumption (%)")
plt.title("Relative Share of Energy Sources Over Time")
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
plt.grid(True)

# Set x-axis limits to actual data
plt.xlim(df_percent.index.min(), df_percent.index.max())

# Ensure latest year appears as x-axis tick
ticks = plt.gca().get_xticks()
ticks = [int(t) for t in ticks if df_percent.index.min() <= t <= df_percent.index.max()]
if df_percent.index.max() not in ticks:
    ticks.append(df_percent.index.max())
plt.xticks(sorted(ticks))

# Show the plot
plt.show()