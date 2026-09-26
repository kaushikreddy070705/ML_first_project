from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def valid_customer():

    return {
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


def test_root():

    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == (
        "Customer Churn Prediction API is running"
    )


def test_health():

    response = client.get("/health")

    assert response.status_code == 200

    assert response.json() == {
        "status": "healthy"
    }


def test_model_info():

    response = client.get("/model-info")

    assert response.status_code == 200

    data = response.json()

    assert data["model"] == "XGBoost"
    assert data["version"] == "tuned"
    assert data["threshold"] == 0.50


def test_prediction_endpoint():

    response = client.post(
        "/predict",
        json=valid_customer()
    )

    assert response.status_code == 200

    data = response.json()

    assert "churn_probability" in data
    assert "prediction" in data
    assert "risk_level" in data

    assert 0 <= data["churn_probability"] <= 1

    assert data["prediction"] in [
        "Yes",
        "No"
    ]

    assert data["risk_level"] in [
        "Low",
        "Medium",
        "High"
    ]


def test_invalid_prediction_request():

    data = valid_customer()

    data["tenure"] = -10

    response = client.post(
        "/predict",
        json=data
    )

    assert response.status_code == 422