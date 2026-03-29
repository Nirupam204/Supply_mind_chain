import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("supplymind_unified_dataset.csv")

# Convert dates to datetime
df["Scheduled Delivery Date"] = pd.to_datetime(df["Scheduled Delivery Date"], errors='coerce')
df["Delivered to Client Date"] = pd.to_datetime(df["Delivered to Client Date"], errors='coerce')

# Create delivery time
df["delivery_time"] = (df["Delivered to Client Date"] - df["Scheduled Delivery Date"]).dt.days

# Fill missing
df["delivery_time"] = df["delivery_time"].fillna(df["delivery_time"].median())
df["freight_cost"] = df["freight_cost"].fillna(df["freight_cost"].median())
df["customer_rating"] = df["customer_rating"].fillna(df["customer_rating"].median())

# Create vendor score (IMPORTANT)
df["vendor_score_calc"] = (
    0.5 * df["customer_rating"] +
    0.3 * (1 / (df["freight_cost"] + 1)) +
    0.2 * (1 / (df["delivery_time"] + 1))
)

# Create label
df["best_vendor_label"] = (df["vendor_score_calc"] > df["vendor_score_calc"].median()).astype(int) # Label 1 for good vendors, 0 for others

# Features
features = ["customer_rating", "freight_cost", "delivery_time"]

X = df[features]
y = df["best_vendor_label"]

# Train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# Save
joblib.dump(model, "best_vendor_model.pkl")

print("Vendor model trained successfully")