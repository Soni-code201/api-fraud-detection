import joblib
import numpy as np

model = joblib.load("model/model.pkl")

sample = [50000, 23, 1, 1, 10, 2, 100]

pred = model.predict([sample])[0]
prob = model.predict_proba([sample])[0][1]

print({"fraud": bool(pred), "probability": float(prob)})