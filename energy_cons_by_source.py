import matplotlib.pyplot as plt
import pandas as pd

file_path = "./datasets/global-energy-substitution.csv"  # Update with the actual file path
df = pd.read_csv(file_path)

# Drop irrelevant columns if they exist
df = df.drop(columns=["Entity", "Code"], errors="ignore")
# Drop rows with missing values
df = df.dropna()

# Convert 'Year' column to integer
df["Year"] = pd.to_numeric(df["Year"], errors="coerce").astype("Int64")

# Convert all other columns to numeric
for col in df.columns:
    if col != "Year":
        df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna(subset=["Year"])
df = df.fillna(0)

df["Year"] = df["Year"].astype(int)
df.set_index("Year", inplace=True)

df.columns = df.columns.map(str)

# Reverse column order so large sources are at the bottom
columns_reversed = df.columns[::-1]
# Plot
plt.figure(figsize=(12, 6))
plt.stackplot(df.index, *[df[col] for col in columns_reversed], labels=columns_reversed, alpha=0.7)
# Reverse legend entries to match stack order
handles, labels = plt.gca().get_legend_handles_labels()
plt.legend(handles[::-1], labels[::-1], loc="upper left", bbox_to_anchor=(1, 1))

plt.xlabel("Year")
plt.ylabel("Energy Consumption (TWh)")
plt.title("Global Energy Consumption Trends Over Time")
# Reverse legend to match top-down order in stackplot
handles, labels = plt.gca().get_legend_handles_labels()
plt.legend(handles[::-1], labels[::-1], loc="upper left", bbox_to_anchor=(1, 1))

plt.grid(True)

# Set x-axis limits to dataset range
plt.xlim(df.index.min(), df.index.max())

# Ensure latest year appears on x-axis
ticks = plt.gca().get_xticks()
ticks = [int(t) for t in ticks if df.index.min() <= t <= df.index.max()]
if df.index.max() not in ticks:
    ticks.append(df.index.max())
plt.xticks(sorted(ticks))

plt.show()