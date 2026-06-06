import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Dummy dataset
data = {
    "amount": [500, 20000, 1500, 70000, 300, 45000],
    "time": [10, 23, 14, 2, 9, 1],
    "location_change": [0,1,0,1,0,1],
    "device_change": [0,1,0,1,0,1],
    "transaction_count": [2,15,3,20,1,12],
    "failed_attempts": [0,3,0,5,0,4],
    "account_age": [365,50,200,30,400,60],
    "fraud": [0,1,0,1,0,1]
}

df = pd.DataFrame(data)

X = df.drop("fraud", axis=1)
y = df["fraud"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "model/model.pkl")

print("Model trained successfully!")