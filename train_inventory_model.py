import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("supplymind_unified_dataset.csv")

# Create target (IMPORTANT)
df["optimal_stock"] = df["sales"] * 1.2

features = [
    "sales",
    "sales_7day_avg",
    "sales_30day_avg",
    "demand_growth",
    "inventory_proxy"
]

X = df[features]
y = df["optimal_stock"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor(n_estimators=100)
model.fit(X_train, y_train)

joblib.dump(model, "best_inventory_model.pkl")

print("Inventory model trained successfully")