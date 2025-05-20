# Emerging Sources (Oil, Gas, Hydro) – Late bloomers; their growth started only around the 1870s–1890s.
import pandas as pd
import matplotlib.pyplot as plt

# Load data
file_path = "./datasets/global-energy-substitution.csv"  
df = pd.read_csv(file_path)
# Extract data
years = df["Year"]
oil = df["Oil (TWh, substituted energy)"]
gas = df["Gas (TWh, substituted energy)"]
hydro = df["Hydropower (TWh, substituted energy)"]

# Create stream graph using stackplot with baseline='wiggle'
plt.figure(figsize=(10, 6))
plt.stackplot(
    years,
    oil, gas, hydro,
    labels=["Oil", "Gas", "Hydropower"],
    colors=["darkred", "teal", "royalblue"],
    alpha=0.8,
    baseline='wiggle'  # this gives it the stream effect
    # baseline='zero'
)

# Formatting
plt.title("Stream Graph of Emerging Energy Sources", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Energy Consumption (TWh, substituted)", fontsize=12)
plt.legend(loc="upper left")
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.show()
