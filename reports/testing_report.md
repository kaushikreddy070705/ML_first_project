# Testing & Quality Assurance Report

## 1. Objective

The objective of this phase was to verify the reliability, correctness, and stability of the Customer Churn Prediction System across unit, schema, and API integration levels.

## 2. Testing Levels

The system was tested at the following levels:

- **Unit Testing:** Validating model file integrity, prediction loading, output format, and risk thresholds.
- **Schema Validation Testing:** Ensuring Pydantic correctly rejects invalid or out-of-bound inputs.
- **API Testing:** Verifying FastAPI endpoints, HTTP response status codes, and error payloads using `TestClient`.
- **Manual Streamlit Testing:** Checking frontend UI behavior, probability gauges, prediction history, and API failure handling.

## 3. Automated Test Suite Breakdown

### Unit Tests (`tests/test_predictor.py`)
- Model file existence check (`xgboost_tuned.joblib`)
- Model loading test via `joblib`
- Prediction payload output structure check
- Probability range assertion ($0 \le p \le 1$)
- Label consistency verification (`Yes` / `No`)
- Risk level boundary classification (`Low`, `Medium`, `High`)

### Schema Tests (`tests/test_schemas.py`)
- Valid customer input schema instantiation
- Rejection of invalid `SeniorCitizen` values
- Rejection of negative `tenure` values
- Rejection of negative `MonthlyCharges` values

### API Tests (`tests/test_api.py`)
- Root endpoint status check (`GET /`)
- Health check endpoint status (`GET /health`)
- Model metadata endpoint response (`GET /model-info`)
- Valid prediction request (`POST /predict`)
- Invalid prediction request handling (`HTTP 422 Unprocessable Entity`)

---

## 4. Manual UI Testing (Streamlit Dashboard)

- **API Status:** Verified sidebar status indicator (`🟢 API Online` / `🔴 API Offline`).
- **Customer Form:** Tested user inputs for demographic, service, and contract attributes.
- **Visualizations:** Confirmed rendering of the Plotly Probability Gauge and Churn vs. Stay Bar Chart.
- **Prediction History:** Verified session-state history logging and clearing functionality.
- **Error Resiliency:** Confirmed Streamlit displays connection alerts gracefully when FastAPI is stopped, without crashing the frontend.

---

## 5. Execution Summary

To run all automated tests, activate the virtual environment and execute:

```powershell
pytest -v