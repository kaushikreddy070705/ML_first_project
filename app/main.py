from fastapi import FastAPI, HTTPException
from app.logging_config import setup_logging
from app.predictor import predict_churn
from app.schemas import CustomerData, PredictionResponse
from app.config import MODEL_NAME, PREDICTION_THRESHOLD

# Initialize logging configuration
setup_logging()

app = FastAPI(title="Customer Churn Prediction API")

@app.get("/")
def root():
    return {"message": "Customer Churn Prediction API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/predict", response_model=PredictionResponse)
def predict(customer: CustomerData):
    try:
        return predict_churn(customer.model_dump())
    except Exception:
        raise HTTPException(status_code=500, detail="Prediction service failed.")

@app.get("/model-info")
def model_info():
    return {
        "model": "XGBoost",
        "version": "tuned",
        "model_file": MODEL_NAME,
        "threshold": PREDICTION_THRESHOLD
    }