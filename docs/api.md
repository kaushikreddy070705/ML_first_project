# Customer Churn Prediction API

## Purpose

This API exposes the trained customer churn prediction model.

## Base URL

http://127.0.0.1:8000

## Endpoints

### GET /

Checks whether the API is running.

### GET /health

Returns API health status.

### POST /predict

Accepts customer information and returns:

- churn probability
- churn prediction
- risk level

### GET /model-info

Returns basic deployed model information.

## Architecture

Customer JSON
→ FastAPI
→ Pydantic validation
→ Saved ML Pipeline
→ XGBoost
→ Prediction probability
→ Threshold
→ JSON response

