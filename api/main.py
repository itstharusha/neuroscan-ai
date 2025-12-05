
from fastapi import FastAPI, HTTPException
from api.schemas import PredictRequest
from src.model_utils import load_objects, preprocess_input, predict
import uvicorn

app = FastAPI(title="NeuroScan API v1")

model, scaler, encoders, schema = None, None, None, None

@app.on_event("startup")
def startup_event():
    global model, scaler, encoders, schema
    model, scaler, encoders, schema = load_objects()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict_endpoint(req: PredictRequest):
    try:
        raw = req.__root__
        X = preprocess_input(raw, scaler, encoders, schema)
        result = predict(model, X)
        return {"risk_score": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)
