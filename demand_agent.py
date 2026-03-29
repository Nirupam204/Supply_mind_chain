import joblib
import pandas as pd

class DemandAgent:
    def __init__(self):
        self.model = joblib.load("best_model.pkl")
        self.columns = joblib.load("columns.pkl")
        self.scaler = joblib.load("scaler.pkl")

    def predict(self, input_data):
        if not isinstance(input_data, dict):
            raise ValueError("Input must be a dictionary")

        df = pd.DataFrame([input_data])

        for col in self.columns:
            if col not in df:
                df[col] = 0

        df = df[self.columns]

        df = self.scaler.transform(df)

        prediction = self.model.predict(df)

        return prediction[0]
