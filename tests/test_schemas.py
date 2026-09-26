import pytest
from pydantic import ValidationError

from app.schemas import CustomerData
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
def test_valid_customer_data():

    customer = CustomerData(
        **valid_customer()
    )

    assert customer.gender == "Female"
    assert customer.tenure == 5

def test_invalid_senior_citizen():

    data = valid_customer()

    data["SeniorCitizen"] = 2

    with pytest.raises(ValidationError):

        CustomerData(**data)

def test_negative_tenure():

    data = valid_customer()

    data["tenure"] = -1

    with pytest.raises(ValidationError):

        CustomerData(**data)

def test_negative_monthly_charges():

    data = valid_customer()

    data["MonthlyCharges"] = -10

    with pytest.raises(ValidationError):

        CustomerData(**data)

