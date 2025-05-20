import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load data
file_path = "./datasets/primary-energy-cons.csv"  
df = pd.read_csv(file_path)

# Pivot: countries as rows, years as columns
growth_df = df.pivot_table(index="Entity", columns="Year", values="Primary energy consumption (TWh)")
growth_df = growth_df.dropna(thresh=30).ffill(axis=1).bfill(axis=1)

# Normalize each country's data (row-wise min-max)
growth_normalized = (growth_df.T - growth_df.min(axis=1)) / (growth_df.max(axis=1) - growth_df.min(axis=1))
growth_normalized = growth_normalized.T.fillna(0)

# Apply KMeans clustering
kmeans = KMeans(n_clusters=4, random_state=42)
cluster_labels = kmeans.fit_predict(growth_normalized)
growth_normalized["Cluster"] = cluster_labels

# Separate cluster labels and data
growth_normalized_no_cluster = growth_normalized.drop(columns=["Cluster"])
countries_with_clusters = growth_normalized[["Cluster"]].reset_index()

# Sample 3 countries per cluster
sampled_countries = countries_with_clusters.groupby("Cluster").apply(
    lambda x: x.sample(min(3, len(x)), random_state=42)
).reset_index(drop=True)

# Plot the sampled countries
plt.figure(figsize=(14, 10))
for _, row in sampled_countries.iterrows():
    country = row["Entity"]
    cluster = row["Cluster"]
    curve = growth_normalized_no_cluster.loc[country]
    plt.plot(curve.index, curve.values, label=f"{country} (Cluster {cluster})")

plt.title("Sample Energy Consumption Growth Curves by Cluster")
plt.xlabel("Year")
plt.ylabel("Normalized Energy Consumption")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
