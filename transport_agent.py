import joblib
import pandas as pd

class TransportAgent:
    def __init__(self):
        self.model = joblib.load("best_transport_model.pkl")

    def select_transport(self, options):
        df = pd.DataFrame(options)

        df = df.rename(columns={"cost": "freight_cost"})

        preds = self.model.predict(df[["freight_cost", "delivery_time"]])

        df["prediction"] = preds

        best_rows = df[df["prediction"] == 1]

        if len(best_rows) == 0:
            best_option = df.sort_values(
                by=["freight_cost", "delivery_time"]
            ).iloc[0]
        else:
            best_option = best_rows.sort_values(
                by=["freight_cost", "delivery_time"]
            ).iloc[0]
            
        return best_option.to_dict()