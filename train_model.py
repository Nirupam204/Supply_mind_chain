from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

def train_models(X_train,y_train):
    lr=LinearRegression()
    lr.fit(X_train,y_train)

    rf=RandomForestRegressor(n_estimators=100)
    rf.fit(X_train,y_train)

    xgb=XGBRegressor()
    xgb.fit(X_train,y_train)

    return lr,rf,xgb