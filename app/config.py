import os
from pathlib import Path

from dotenv import load_dotenv


# ============================================================
# PROJECT ROOT
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

load_dotenv(BASE_DIR / ".env")


# ============================================================
# API CONFIGURATION
# ============================================================

API_HOST = os.getenv(
    "API_HOST",
    "127.0.0.1"
)

API_PORT = int(
    os.getenv(
        "API_PORT",
        "8000"
    )
)


# ============================================================
# MODEL CONFIGURATION
# ============================================================

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "xgboost_tuned.joblib"
)

MODEL_PATH = (
    BASE_DIR
    / "models"
    / MODEL_NAME
)


# ============================================================
# PREDICTION CONFIGURATION
# ============================================================

PREDICTION_THRESHOLD = float(
    os.getenv(
        "PREDICTION_THRESHOLD",
        "0.50"
    )
)


# ============================================================
# RISK THRESHOLDS
# ============================================================

MEDIUM_RISK_THRESHOLD = float(
    os.getenv(
        "MEDIUM_RISK_THRESHOLD",
        "0.40"
    )
)

HIGH_RISK_THRESHOLD = float(
    os.getenv(
        "HIGH_RISK_THRESHOLD",
        "0.70"
    )
)


# ============================================================
# LOGGING
# ============================================================

LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO"
)