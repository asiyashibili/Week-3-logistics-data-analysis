import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seed for reproducibility
np.random.seed(42)
n_shipments = 1000

# Generate synthetic dataset
data = {
    "Shipment_ID": [f"SHIP_{i:04d}" for i in range(1, n_shipments + 1)],
    "Carrier": np.random.choice(["Carrier A", "Carrier B", "Carrier C"], size=n_shipments, p=[0.40, 0.35, 0.25]),
    "Origin": np.random.choice(["Hub East", "Hub West", "Hub North"], size=n_shipments),
    "Destination": np.random.choice(["City X", "City Y", "City Z"], size=n_shipments),
    "Distance_km": np.random.uniform(100, 2500, size=n_shipments).round(2),
    "Shipment_Weight_kg": np.random.uniform(10, 500, size=n_shipments).round(2),
    "Planned_Delivery_Days": np.random.randint(2, 7, size=n_shipments)
}

df = pd.DataFrame(data)

# Simulate delivery delays and calculate costs
df["Actual_Delivery_Days"] = df["Planned_Delivery_Days"] + np.random.choice(
    [0, 1, 2, 3, 5], size=n_shipments, p=[0.55, 0.25, 0.10, 0.07, 0.03]
)
df["Delay_Days"] = df["Actual_Delivery_Days"] - df["Planned_Delivery_Days"]

df["Transportation_Cost_USD"] = (
    50 + (df["Distance_km"] * 0.45) + (df["Shipment_Weight_kg"] * 0.85) + 
    (df["Delay_Days"] * 30) + np.random.normal(0, 25, size=n_shipments)
).round(2)

# Visualization 1: Cost vs Distance
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Distance_km", y="Transportation_Cost_USD", hue="Carrier", alpha=0.7)
sns.regplot(data=df, x="Distance_km", y="Transportation_Cost_USD", scatter=False, color="black")
plt.title("Transportation Cost vs. Distance by Carrier")
plt.xlabel("Distance (km)")
plt.ylabel("Transportation Cost ($)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("cost_vs_distance.png")
plt.close()

# Visualization 2: Delay Distribution
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Carrier", y="Delay_Days", palette="Set2")
plt.title("Delivery Delay Distribution Across Logistics Carriers")
plt.xlabel("Carrier")
plt.ylabel("Delay (Days)")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("carrier_delays.png")
plt.close()

# Visualization 3: Correlation Matrix
plt.figure(figsize=(7, 5))
numeric_cols = ["Distance_km", "Shipment_Weight_kg", "Planned_Delivery_Days", "Actual_Delivery_Days", "Delay_Days", "Transportation_Cost_USD"]
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="Coolwarm", fmt=".2f")
plt.title("Logistics Metrics Correlation Matrix")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.close()

print("Data processing and visualization complete!")