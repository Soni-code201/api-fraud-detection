# 💳 UPI Fraud Detection System

A Machine Learning-based fraud detection system that identifies suspicious UPI transactions using transaction-related features. The project uses a Random Forest Classifier for prediction, FastAPI for backend services, and Streamlit for the user interface.

---

## 🚀 Features

- Detect fraudulent UPI transactions
- Machine Learning model using Random Forest Classifier
- FastAPI REST API integration
- Streamlit interactive dashboard
- Fraud probability prediction
- Easy-to-use frontend interface

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- FastAPI
- Streamlit
- Joblib

---

## 📂 Project Structure

```bash
UPI-Fraud-Detection/
│
├── app.py              # FastAPI backend
├── train.py            # Model training script
├── predict.py          # Fraud prediction script
├── ui.py               # Streamlit frontend
│
├── model/
│   └── model.pkl       # Trained model
│
└── README.md
```

---

## 📊 Input Features

The model predicts fraud based on the following transaction details:

- Transaction Amount
- Transaction Time
- Location Change
- Device Change
- Transaction Count
- Failed Login Attempts
- Account Age

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/UPI-Fraud-Detection.git
cd UPI-Fraud-Detection
```

Install dependencies:

```bash
pip install pandas numpy scikit-learn fastapi uvicorn streamlit joblib requests
```

---

## 🏋️ Train the Model

Run the training script:

```bash
python train.py
```

Output:

```text
Model trained successfully!
```

The trained model will be saved as:

```text
model/model.pkl
```

---

## ▶️ Run FastAPI Backend

Start the API server:

```bash
uvicorn app:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

## 🖥️ Run Streamlit Frontend

Launch the Streamlit application:

```bash
streamlit run ui.py
```

---

## 🔍 API Endpoints

### Home Endpoint

```http
GET /
```

Response:

```json
{
  "message": "UPI Fraud Detection API"
}
```

### Prediction Endpoint

```http
GET /predict
```

Sample Response:

```json
{
  "fraud": true,
  "probability": 0.92
}
```

---

## 🤖 Machine Learning Model

**Algorithm Used:** Random Forest Classifier

Why Random Forest?

- Handles complex patterns efficiently
- Good performance on tabular data
- Reduces overfitting
- Provides probability-based predictions

---

## 🎯 Future Improvements

- Real-world UPI transaction dataset integration
- User authentication and authorization
- Database connectivity
- Real-time fraud monitoring
- Advanced ML models for improved accuracy
- Cloud deployment (AWS, Azure, Render)

---

## 👩‍💻 Author

**Soni Yadav**

B.Tech – Computer Science & Engineering

Interested in Machine Learning, Data Analytics, and Software Development.

---

## 📜 License

This project is developed for educational and learning purposes.
