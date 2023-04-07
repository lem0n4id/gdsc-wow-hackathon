
import xgboost as xg


def saved():
    model = xg.XGBRegressor()
    model.load_model("model4.json")

    return model
