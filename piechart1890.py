#Pie Chart (1890) – Clearly shows traditional biomass and coal dominated, while others were negligible.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
file_path = "./datasets/global-energy-substitution.csv"  
df = pd.read_csv(file_path)

# Filter for 1890 data
row_1890 = df[df["Year"] == 1890].iloc[0]
labels = [
    "Other renewables (TWh, substituted energy)",
    "Biofuels (TWh, substituted energy)",
    "Solar (TWh, substituted energy)",
    "Wind (TWh, substituted energy)",
    "Hydropower (TWh, substituted energy)",
    "Nuclear (TWh, substituted energy)",
    "Gas (TWh, substituted energy)",
    "Oil (TWh, substituted energy)",
    "Coal (TWh, substituted energy)",
    "Traditional biomass (TWh, substituted energy)"
]
values = row_1890[labels].values
percentages = values / values.sum() * 100
short_labels = [label.split()[0] for label in labels]
formatted_labels = [f"{short_labels[i]}: {percentages[i]:.1f}%" for i in range(len(labels))]

# Plot pie chart
fig, ax = plt.subplots(figsize=(12, 8))
wedges, _ = ax.pie(values, startangle=140, radius=1.1)

# Compute angles and positions
angles = [(w.theta2 + w.theta1) / 2 for w in wedges]
positions = [{"angle": a, "index": i} for i, a in enumerate(angles) if values[i] > 0]

# Split into left and right side
left = [p for p in positions if np.cos(np.radians(p["angle"])) < 0]
right = [p for p in positions if np.cos(np.radians(p["angle"])) >= 0]

# Sort by vertical position
left.sort(key=lambda p: np.sin(np.radians(p["angle"])))
right.sort(key=lambda p: np.sin(np.radians(p["angle"])))

# Y positions
def spaced_y(n, center=0, spacing=0.25):
    return [center + spacing * (i - (n - 1) / 2) for i in range(n)]

left_y = spaced_y(len(left))
right_y = spaced_y(len(right))

# Draw labels with arrows
for side, y_positions in zip([left, right], [left_y, right_y]):
    for pos, y in zip(side, y_positions):
        i = pos["index"]
        angle = pos["angle"]
        x = np.cos(np.radians(angle))
        y_offset = np.sin(np.radians(angle))
        x_label = -1.8 if x < 0 else 1.8
        ha = "right" if x < 0 else "left"

        if i < len(formatted_labels):
            ax.annotate(
                formatted_labels[i],
                xy=(x, y_offset),
                xytext=(x_label, y),
                ha=ha,
                va="center",
                arrowprops=dict(arrowstyle="-", connectionstyle="angle3")
            )

plt.title("Share of Energy Sources in 1890")
plt.tight_layout()
plt.show()