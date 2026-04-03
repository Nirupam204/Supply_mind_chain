import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from train_model import train_models
from evaluate import evaluate_model
from sklearn.preprocessing import StandardScaler
import joblib

print("Loading data...")

df=pd.read_csv("supplymind_unified_dataset.csv")

target="sales"

df=df.dropna()
df=df.drop(columns=["date"])
df=df.select_dtypes(include=['number'])

X=df.drop(columns=[target])
y=df[target]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

print("Training models...")

lr,rf,xgb=train_models(X_train,y_train)

print("Evaluating...")

lr_mae,lr_rmse=evaluate_model(y_test,lr.predict(X_test))
rf_mae,rf_rmse=evaluate_model(y_test,rf.predict(X_test))
xgb_mae,xgb_rmse=evaluate_model(y_test,xgb.predict(X_test))

results = {
    "LR": (lr, lr_rmse),
    "RF": (rf, rf_rmse),
    "XGB": (xgb, xgb_rmse)
}

best_model_name = min(results, key=lambda x: results[x][1])
best_model = results[best_model_name][0]

joblib.dump(best_model, "best_model.pkl") #saved the file into best_model.pkl
joblib.dump(X.columns.tolist(), "columns.pkl")
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

joblib.dump(scaler, "scaler.pkl")
print("Best Model:", best_model_name)
print("Model saved as best_model.pkl")