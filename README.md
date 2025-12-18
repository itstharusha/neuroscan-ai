# 🧠 NeuroScan AI  
### End-to-End Autism Screening Risk Prediction API  
**Machine Learning · FastAPI · Docker · AWS ECS**

---

## 📌 Overview

**NeuroScan AI** is a production-ready machine learning system designed to predict **Autism Spectrum Disorder (ASD) screening risk** using structured behavioral and demographic data.

This project demonstrates a **full real-world ML lifecycle**:
- Data preprocessing & feature engineering  
- Model training and evaluation  
- Model serialization  
- REST API development using FastAPI  
- Containerization with Docker  
- Cloud deployment readiness (AWS ECS Fargate)

The system exposes a `/predict` endpoint that accepts structured JSON input and returns a **risk score** for ASD.

---

## 🎯 Problem Statement

Early screening for Autism Spectrum Disorder is critical, but manual assessments can be time-consuming and resource-intensive.

**Goal:**  
Build an automated, scalable, and deployable ML system that assists in early ASD risk screening using questionnaire-based data.

---

## 🧠 Machine Learning Details

- **Dataset**: Autism Screening for Toddlers (Kaggle)
- **Model**: Random Forest Classifier
- **Preprocessing**:
  - Missing value handling
  - Label encoding for categorical features
  - Feature scaling with `StandardScaler`
- **Evaluation Metrics**:
  - Precision
  - Recall
  - F1-Score
  - Confusion Matrix
- **Model Export**: `joblib`

> ⚠️ Note: High accuracy is expected due to dataset size and structure. Real-world deployment should include further validation.

---

## 🏗️ Project Architecture

neuroscan-ai/
├── api/
│ ├── main.py # FastAPI application
│ └── schemas.py # Request schemas
├── src/
│ └── model_utils.py # Model loading & preprocessing
├── models/
│ ├── neuro_model_v1.joblib
│ ├── scaler.joblib
│ └── label_encoders.joblib
├── input_schema.txt # Feature order reference
├── requirements.txt
├── Dockerfile
└── README.md

yaml
Copy code

---

## 🚀 API Endpoints

### 🔹 Health Check
GET /health

pgsql
Copy code

**Response**
```json
{ "status": "ok" }
🔹 Prediction
bash
Copy code
POST /predict
Request Body

json
Copy code
{
  "Sex": "m",
  "A1_Score": 1,
  "A2_Score": 0,
  "A3_Score": 1,
  "...": "..."
}
Response

json
Copy code
{
  "risk_score": 0.87
}
risk_score represents the probability of ASD risk.
