import pandas as pd
import matplotlib.pyplot as plt

# Load data
file_path = "./datasets/primary-energy-cons.csv"  
df = pd.read_csv(file_path)

# Compute Year-over-Year (YoY) Change
df_sorted = df.sort_values(by=["Entity", "Year"])
df_sorted["YoY Change"] = df_sorted.groupby("Entity")["Primary energy consumption (TWh)"].diff()

# Select example countries to visualize
example_countries = ["Afghanistan", "United States", "Germany", "China", "Brazil"]
filtered_df = df_sorted[df_sorted["Entity"].isin(example_countries)]

# Plotting
plt.figure(figsize=(14, 8))

for country in example_countries:
    country_data = filtered_df[filtered_df["Entity"] == country]
    plt.plot(country_data["Year"], country_data["YoY Change"], label=country)

plt.title("Year-over-Year Change in Energy Consumption")
plt.xlabel("Year")
plt.ylabel("YoY Change (TWh)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()