import logging
import joblib
import pandas as pd
from app.config import (
    HIGH_RISK_THRESHOLD,
    MEDIUM_RISK_THRESHOLD,
    MODEL_PATH,
    PREDICTION_THRESHOLD,
)

logger = logging.getLogger(__name__)

logger.info("Loading model from: %s", MODEL_PATH)
model = joblib.load(MODEL_PATH)
logger.info("Model loaded successfully.")

def get_risk_level(probability: float) -> str:
    if probability >= HIGH_RISK_THRESHOLD:
        return "High"
    if probability >= MEDIUM_RISK_THRESHOLD:
        return "Medium"
    return "Low"

def predict_churn(customer_data: dict):
    logger.info("Received prediction request.")
    customer_df = pd.DataFrame([customer_data])
    probability = float(model.predict_proba(customer_df)[0, 1])
    
    prediction = "Yes" if probability >= PREDICTION_THRESHOLD else "No"
    risk_level = get_risk_level(probability)
    
    logger.info("Prediction completed successfully.")
    return {
        "churn_probability": round(probability, 4),
        "prediction": prediction,
        "risk_level": risk_level,
    }