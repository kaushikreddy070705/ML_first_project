import logging

from fastapi import FastAPI

from app.predictor import predict_churn
from app.schemas import CustomerData, PredictionResponse


# ============================================================
# LOGGING CONFIGURATION
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(name)s | "
        "%(message)s"
    )
)

logger = logging.getLogger(__name__)


# ============================================================
# FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="Customer Churn Prediction API",
    description=(
        "API for predicting telecom customer churn."
    ),
    version="1.0.0"
)


# ============================================================
# ROOT
# ============================================================

@app.get("/")
def root():

    logger.info(
        "Root endpoint accessed."
    )

    return {
        "message": (
            "Customer Churn Prediction API "
            "is running"
        )
    }


# ============================================================
# HEALTH
# ============================================================

@app.get("/health")
def health():

    logger.info(
        "Health check requested."
    )

    return {
        "status": "healthy"
    }


# ============================================================
# PREDICTION
# ============================================================

@app.post(
    "/predict",
    response_model=PredictionResponse
)
def predict(customer: CustomerData):

    logger.info(
        "Prediction endpoint called."
    )

    result = predict_churn(
        customer.model_dump()
    )

    logger.info(
        "Prediction endpoint completed."
    )

    return result


# ============================================================
# MODEL INFORMATION
# ============================================================

@app.get("/model-info")
def model_info():

    logger.info(
        "Model information requested."
    )

    return {
        "model": "XGBoost",
        "version": "tuned",
        "threshold": 0.50
    }