import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load data
file_path = "./datasets/primary-energy-cons.csv"  
df = pd.read_csv(file_path)

# Select a country for analysis
country = "Germany"
country_data = df[df["Entity"] == country].sort_values(by="Year")

# Extract years and energy consumption
years = country_data["Year"].values.reshape(-1, 1)
consumption = country_data["Primary energy consumption (TWh)"].values

# Fit a linear regression model to detect trend
model = LinearRegression()
model.fit(years, consumption)
trend = model.predict(years)

# Calculate residuals (difference from trend)
residuals = consumption - trend
std_dev = np.std(residuals)

# Identify breakpoints where residual > 2 standard deviations
break_indices = np.nonzero(np.abs(residuals) > 2 * std_dev)[0]
break_years = years[break_indices].flatten()

# Plot the time series with trend and "x" markers for breaks
plt.figure(figsize=(12, 6))
plt.plot(years.flatten(), consumption, color="#f4c542", label="Actual Consumption")
plt.plot(years.flatten(), trend, color="#ff6600", label="Linear Trend", linestyle="--")
plt.scatter(break_years, consumption[break_indices], color="red", marker="x", s=100, label="Detected Break", zorder=5)
plt.title(f"Manual Structural Break Detection: {country}")
plt.xlabel("Year")
plt.ylabel("Energy Consumption (TWh)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Output the detected break years
print("Detected Structural Break Years:", list(break_years))