from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("model/model.pkl")

@app.get("/")
def home():
    return {"message": "UPI Fraud Detection API"}

@app.get("/predict")
def predict():
    sample = [50000, 23, 1, 1, 10, 2, 100]
    pred = model.predict([sample])[0]
    prob = model.predict_proba([sample])[0][1]
    return {"fraud": bool(pred), "probability": float(prob)}