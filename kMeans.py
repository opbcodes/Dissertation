import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load data
file_path = "./datasets/primary-energy-cons.csv"  
df = pd.read_csv(file_path)

# Pivot to get years as columns, countries as rows
growth_df = df.pivot_table(index="Entity", columns="Year", values="Primary energy consumption (TWh)")

# Filter countries with data for at least 30 years
growth_df = growth_df.dropna(thresh=30)

# Fill missing values with forward and backward fill
growth_df = growth_df.ffill(axis=1).bfill(axis=1)

# Normalize each country's data (min-max scaling row-wise)
growth_normalized = (growth_df.T - growth_df.min(axis=1)) / (growth_df.max(axis=1) - growth_df.min(axis=1))
growth_normalized = growth_normalized.T.fillna(0)

# Apply KMeans clustering to growth curves
kmeans = KMeans(n_clusters=4, random_state=42)
cluster_labels = kmeans.fit_predict(growth_normalized)

# Attach cluster labels to countries
growth_normalized["Cluster"] = cluster_labels

# Extract cluster centroids
centroids = kmeans.cluster_centers_

# Prepare centroids for plotting
years = growth_df.columns
centroid_df = pd.DataFrame(centroids, columns=years)
centroid_df["Cluster"] = centroid_df.index

centroid_df = pd.melt(centroid_df, id_vars="Cluster", var_name="Year", value_name="Normalized Consumption")
centroid_df["Year"] = centroid_df["Year"].astype(int)

# Plot the cluster centroids (growth typologies)
plt.figure(figsize=(12, 7))
for cluster_id in centroid_df["Cluster"].unique():
    cluster_data = centroid_df[centroid_df["Cluster"] == cluster_id]
    plt.plot(cluster_data["Year"], cluster_data["Normalized Consumption"], label=f"Cluster {cluster_id}")

plt.title("Cluster Centroids: Energy Consumption Growth Typologies")
plt.xlabel("Year")
plt.ylabel("Normalized Energy Consumption")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()