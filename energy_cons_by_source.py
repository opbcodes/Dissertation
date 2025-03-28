import matplotlib.pyplot as plt
import pandas as pd

file_path = "./datasets/global-energy-substitution.csv"  # Update with the actual file path
df = pd.read_csv(file_path)

# Drop rows with missing values
df = df.dropna()

# Convert 'Year' column to integer
df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")

# Convert all other columns to numeric
for col in df.columns:
    if col != "Year":
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Drop rows with invalid years
df = df.dropna(subset=["Year"])

# Replace remaining NaN values with 0
df = df.fillna(0)

# Convert Year to int and set as index
df["Year"] = df["Year"].astype(int)
df.set_index("Year", inplace=True)

# Ensure column names are strings (just in case)
df.columns = df.columns.map(str)

# Plot
plt.figure(figsize=(12, 6))
plt.stackplot(df.index, *[df[col] for col in df.columns], labels=df.columns, alpha=0.7)

# Labels and Title
plt.xlabel("Year")
plt.ylabel("Energy Consumption (TWh)")
plt.title("Global Energy Consumption Trends Over Time")
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
plt.grid(True)

# Set x-axis limits to dataset range
plt.xlim(df.index.min(), df.index.max())

# Ensure latest year appears on x-axis
ticks = plt.gca().get_xticks()
ticks = [int(t) for t in ticks if df.index.min() <= t <= df.index.max()]
if df.index.max() not in ticks:
    ticks.append(df.index.max())
plt.xticks(sorted(ticks))

# Show Plot
plt.show()