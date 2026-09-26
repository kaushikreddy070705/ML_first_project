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
ENV_FILE = BASE_DIR / ".env"
load_dotenv(ENV_FILE)

# ============================================================
# HELPER FUNCTIONS
# ============================================================
def get_int_env(name: str, default: int) -> int:
    value = os.getenv(name, str(default))
    try:
        return int(value)
    except ValueError as exc:
        raise ValueError(f"{name} must be an integer. Received: {value}") from exc

def get_float_env(name: str, default: float) -> float:
    value = os.getenv(name, str(default))
    try:
        return float(value)
    except ValueError as exc:
        raise ValueError(f"{name} must be a number. Received: {value}") from exc

# ============================================================
# API & MODEL CONFIGURATION
# ============================================================
API_HOST = os.getenv("API_HOST", "127.0.0.1")
API_PORT = get_int_env("API_PORT", 8000)

MODEL_NAME = os.getenv("MODEL_NAME", "xgboost_tuned.joblib")
MODEL_PATH = BASE_DIR / "models" / MODEL_NAME

# ============================================================
# PREDICTION & RISK THRESHOLDS
# ============================================================
PREDICTION_THRESHOLD = get_float_env("PREDICTION_THRESHOLD", 0.50)
MEDIUM_RISK_THRESHOLD = get_float_env("MEDIUM_RISK_THRESHOLD", 0.40)
HIGH_RISK_THRESHOLD = get_float_env("HIGH_RISK_THRESHOLD", 0.70)

# ============================================================
# LOGGING CONFIGURATION (DEFINED HERE)
# ============================================================
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_DIR = BASE_DIR / "logs"
LOG_FILE = LOG_DIR / "app.log"

# ============================================================
# CONFIGURATION VALIDATION
# ============================================================
def validate_config():
    if not 1 <= API_PORT <= 65535:
        raise ValueError("API_PORT must be between 1 and 65535.")
    if not MODEL_NAME:
        raise ValueError("MODEL_NAME cannot be empty.")
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
    if not 0 < PREDICTION_THRESHOLD < 1:
        raise ValueError("PREDICTION_THRESHOLD must be between 0 and 1.")
    if not 0 < MEDIUM_RISK_THRESHOLD < 1:
        raise ValueError("MEDIUM_RISK_THRESHOLD must be between 0 and 1.")
    if not 0 < HIGH_RISK_THRESHOLD < 1:
        raise ValueError("HIGH_RISK_THRESHOLD must be between 0 and 1.")
    if MEDIUM_RISK_THRESHOLD >= HIGH_RISK_THRESHOLD:
        raise ValueError("MEDIUM_RISK_THRESHOLD must be less than HIGH_RISK_THRESHOLD.")

validate_config()