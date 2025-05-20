# Coal vs. Traditional Biomass Line Chart – Coal saw sharp growth over the century, while biomass stayed high but plateaued.
import pandas as pd
import matplotlib.pyplot as plt

# Load data
file_path = "./datasets/global-energy-substitution.csv"  
df = pd.read_csv(file_path)

# Extract data
years = df["Year"]
coal = df["Coal (TWh, substituted energy)"]
biomass = df["Traditional biomass (TWh, substituted energy)"]

# Plot line chart without markers
plt.figure(figsize=(10, 6))
plt.plot(years, coal, label="Coal", color="orange", linewidth=2)
plt.plot(years, biomass, label="Traditional Biomass", color="red", linewidth=2)

# Chart formatting
plt.title("Coal vs Traditional Biomass Usage", fontsize=14)
plt.xlabel("Year", fontsize=12)
plt.ylabel("Energy Consumption (TWh)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()