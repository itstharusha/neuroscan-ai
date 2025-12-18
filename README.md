# NeuroScan AI  
### End-to-End Autism Screening Risk Prediction API  
Machine Learning · FastAPI · Docker · AWS ECS

---

## Overview  

NeuroScan AI is a fully developed machine learning solution designed to predict Autism Spectrum Disorder (ASD) screening risk using structured behavioral and demographic data.

This project demonstrates the entire machine learning lifecycle, including:  
- Data preprocessing and feature engineering  
- Model training and evaluation  
- Model serialization  
- REST API integration using FastAPI  
- Containerization with Docker  
- Cloud deployment preparedness for AWS ECS Fargate  

The API exposes a /predict endpoint that accepts structured JSON data and returns an ASD risk score.

---

## Problem Statement  

Early detection of Autism Spectrum Disorder is crucial, yet manual assessments are often time-consuming and resource-intensive.

Objective: Build an automated, scalable, and deployable machine learning system to assist with early ASD screening using questionnaire-based data.

---

## Machine Learning Details  

- Dataset: Autism Screening for Toddlers (Kaggle)  
- Model: Random Forest Classifier  
- Preprocessing:  
  - Handling missing values  
  - Label encoding for categorical data  
  - Feature scaling using StandardScaler  
- Evaluation Metrics:  
  - Precision  
  - Recall  
  - F1-Score  
  - Confusion Matrix  
- Model Export: Serialized using joblib  

Note: While the dataset yields high accuracy during development, further validation is necessary before real-world deployment.  

---

## Project Architecture  
neuroscan-ai/
├── api/
│   ├── main.py               # FastAPI application
│   └── schemas.py            # Request schemas
├── src/
│   └── model_utils.py        # Model loading & preprocessing
├── models/
│   ├── neuro_model_v1.joblib
│   ├── scaler.joblib
│   └── label_encoders.joblib
├── input_schema.txt          # Reference for feature order
├── requirements.txt
├── Dockerfile
└── README.md

---

## API Endpoints  

### Health Check  
- Method: GET /health  
- Response:  
 
  {
    "status": "ok"
  }
  
---

### Prediction  
- Method: POST /predict  
- Request Body Example:  
 
  {
    "Sex": "m",
    "A1_Score": 1,
    "A2_Score": 0,
    "A3_Score": 1,
    "...": "Additional features here"
  }
  
- Response Example:  
 
  {
    "risk_score": 0.87
  }
   
 
risk_score represents the probability of ASD risk.

---

