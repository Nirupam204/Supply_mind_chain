import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("supplymind_unified_dataset.csv")

# Create delivery_time if not exists
df["Scheduled Delivery Date"] = pd.to_datetime(
    df["Scheduled Delivery Date"],
    format="%m/%d/%y",
    errors='coerce'
)

df["Delivered to Client Date"] = pd.to_datetime(
    df["Delivered to Client Date"],
    format="%m/%d/%y",
    errors='coerce'
)

df["delivery_time"] = (df["Delivered to Client Date"] - df["Scheduled Delivery Date"]).dt.days
df["delivery_time"] = df["delivery_time"].fillna(df["delivery_time"].median())

df["freight_cost"] = df["freight_cost"].fillna(df["freight_cost"].median())

# Create score (IMPORTANT)
df["transport_score"] = (
    0.6 * df["freight_cost"] +
    0.4 * df["delivery_time"]
)

# Create label (lower score = better)
df["best_transport_label"] = (df["transport_score"] < df["transport_score"].median()).astype(int)

# Features
features = ["freight_cost", "delivery_time"]

X = df[features]
y = df["best_transport_label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

joblib.dump(model, "best_transport_model.pkl")

print("Transport model trained successfully")