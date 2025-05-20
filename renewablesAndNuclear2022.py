# Renewables & Nuclear Area Chart – Mostly flat here, indicating almost no role during this era (yet sets the stage for 20th-century expansion).

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
file_path = "./datasets/global-energy-substitution.csv"  
df = pd.read_csv(file_path)

# Filter for 1890
row = df[df["Year"] == 2022].iloc[0]

# Define renewable & nuclear categories
categories = [
    "Hydropower (TWh, substituted energy)",
    "Other renewables (TWh, substituted energy)",
    "Biofuels (TWh, substituted energy)",
    "Solar (TWh, substituted energy)",
    "Wind (TWh, substituted energy)",
    "Nuclear (TWh, substituted energy)"
]

labels = [cat.split()[0] for cat in categories]  # Shorten for display
values = [row[cat] for cat in categories]

# Radar chart setup
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
values += values[:1]  # loop back to start
angles += angles[:1]

# Plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
ax.plot(angles, values, color='green', linewidth=2)
ax.fill(angles, values, color='green', alpha=0.25)
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)
ax.set_title("Renewables and Nuclear Energy in 2022", fontsize=14, pad=20)
plt.tight_layout()
plt.show()