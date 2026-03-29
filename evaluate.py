from sklearn.metrics import mean_absolute_error, mean_squared_error

def evaluate_model(y_test,pred):
    mae=mean_absolute_error(y_test,pred)
    rmse=mean_squared_error(y_test,pred)**0.5
    return mae,rmse