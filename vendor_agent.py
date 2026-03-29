import joblib
import pandas as pd

class VendorAgent:
    def __init__(self):
        self.model = joblib.load("best_vendor_model.pkl")

    def select_vendor(self, vendors):
        df = pd.DataFrame(vendors)

        features = ["customer_rating", "freight_cost", "delivery_time"]

        preds = self.model.predict(df[features])

        df["prediction"] = preds

        best_vendor = df[df["prediction"] == 1].iloc[0]

        return best_vendor.to_dict()