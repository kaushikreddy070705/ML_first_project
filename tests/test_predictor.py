from pathlib import Path
import joblib
from app.predictor import predict_churn, get_risk_level



# ============================================================
# PATH CONFIGURATION
# ============================================================

# Resolves the path to models/xgboost_tuned.joblib relative to project root
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "xgboost_tuned.joblib"


# ============================================================
# MODEL LOADING TESTS
# ============================================================

def test_model_file_exists():
    assert MODEL_PATH.exists(), f"Model file not found at {MODEL_PATH}"


def test_model_can_be_loaded():
    model = joblib.load(MODEL_PATH)
    assert model is not None


# ============================================================
# PREDICTION TESTS
# ============================================================

def test_prediction_returns_expected_keys():
    customer = {
        "gender": "Female",
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "No",
        "tenure": 5,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 80.5,
        "TotalCharges": 400.5
    }

    result = predict_churn(customer)

    assert "churn_probability" in result
    assert "prediction" in result
    assert "risk_level" in result


def test_prediction_probability_is_valid():
    customer = {
        "gender": "Male",
        "SeniorCitizen": 0,
        "Partner": "No",
        "Dependents": "No",
        "tenure": 2,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "Yes",
        "StreamingMovies": "Yes",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 95.0,
        "TotalCharges": 190.0
    }

    result = predict_churn(customer)
    probability = result["churn_probability"]

    assert 0 <= probability <= 1


def test_prediction_label_is_valid():
    customer = {
        "gender": "Female",
        "SeniorCitizen": 1,
        "Partner": "No",
        "Dependents": "No",
        "tenure": 1,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 90.0,
        "TotalCharges": 90.0
    }

    result = predict_churn(customer)

    assert result["prediction"] in ["Yes", "No"]


def test_risk_level_is_valid():
    customer = {
        "gender": "Female",
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "Yes",
        "tenure": 24,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "DSL",
        "OnlineSecurity": "Yes",
        "OnlineBackup": "Yes",
        "DeviceProtection": "Yes",
        "TechSupport": "Yes",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": "Two year",
        "PaperlessBilling": "No",
        "PaymentMethod": "Bank transfer (automatic)",
        "MonthlyCharges": 60.0,
        "TotalCharges": 1440.0
    }

    result = predict_churn(customer)

    assert result["risk_level"] in ["Low", "Medium", "High"]

def get_risk_level(probability):
    if probability >= 0.70:
        return "High"

    if probability >= 0.40:
        return "Medium"

    return "Low"

def test_risk_level_boundaries():

    assert get_risk_level(0.10) == "Low"
    assert get_risk_level(0.39) == "Low"

    assert get_risk_level(0.40) == "Medium"
    assert get_risk_level(0.69) == "Medium"

    assert get_risk_level(0.70) == "High"
    assert get_risk_level(0.95) == "High"