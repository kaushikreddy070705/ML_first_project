from app.config import (
    HIGH_RISK_THRESHOLD,
    MEDIUM_RISK_THRESHOLD,
    MODEL_PATH,
    PREDICTION_THRESHOLD,
)

def test_model_path_exists():
    assert MODEL_PATH.exists()

def test_prediction_threshold_is_valid():
    assert 0 < PREDICTION_THRESHOLD < 1

def test_medium_risk_threshold_is_valid():
    assert 0 < MEDIUM_RISK_THRESHOLD < 1

def test_high_risk_threshold_is_valid():
    assert 0 < HIGH_RISK_THRESHOLD < 1

def test_risk_threshold_order():
    assert MEDIUM_RISK_THRESHOLD < HIGH_RISK_THRESHOLD