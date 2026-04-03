import joblib
import pandas as pd

class InventoryAgent:
    def __init__(self):
        self.model = joblib.load("best_inventory_model.pkl")

    def decide(self, input_data):
        df = pd.DataFrame([input_data])

        features = [
            "sales",
            "sales_7day_avg",
            "sales_30day_avg",
            "demand_growth",
            "inventory_proxy"
        ]

        required_stock = self.model.predict(df[features])[0]

        order_quantity = max(0, required_stock - input_data["inventory_proxy"])

        return {
            "required_stock": round(required_stock, 2),
            "order_quantity": round(order_quantity, 2)
        }
    