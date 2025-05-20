import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
file_path = "./datasets/global-energy-substitution.csv"  
df = pd.read_csv(file_path)

# Select relevant columns and filter for 1800–1890
sources = [
    "Solar (TWh, substituted energy)",
    "Wind (TWh, substituted energy)",
    "Hydropower (TWh, substituted energy)",
    "Biofuels (TWh, substituted energy)",
    "Other renewables (TWh, substituted energy)",
    "Nuclear (TWh, substituted energy)"
]
df = df[(df["Year"] >= 1999) & (df["Year"] <= 2009)]
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df[sources] = df[sources].apply(pd.to_numeric, errors="coerce")

# Prepare data
heatmap_data = df.set_index("Year")[sources].T

# Plot cleaner heatmap
plt.figure(figsize=(12, 5))
sns.heatmap(
    heatmap_data,
    cmap="YlGnBu",
    annot=True, fmt=".1f",
    cbar_kws={"label": "TWh"},
    linewidths=0.3,
    linecolor="gray"
)
plt.title("Renewables & Nuclear Energy (1800–1890)", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Energy Source")
plt.tight_layout()
plt.show()