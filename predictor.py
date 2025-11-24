"""
predictor.py
Simple linear regression predictor stub. Uses scikit-learn if available.
It predicts temperature using previous day's temperature as a feature (very basic).
"""
def predict_temperature(data, days_ahead=1):
    try:
        from sklearn.linear_model import LinearRegression
        import numpy as np
    except Exception as e:
        raise RuntimeError("scikit-learn and numpy required for prediction. Install via requirements.txt") from e

    # prepare features: use previous day's temperature
    X, y = [], []
    for i in range(1, len(data)):
        X.append([data[i-1]["temperature_c"]])
        y.append(data[i]["temperature_c"])
    if not X:
        raise ValueError("Not enough data for prediction")
    model = LinearRegression().fit(X, y)
    last_temp = [[data[-1]["temperature_c"]]]
    preds = []
    cur = last_temp
    for _ in range(days_ahead):
        p = model.predict(cur)[0]
        preds.append(float(p))
        cur = [[p]]
    return preds
