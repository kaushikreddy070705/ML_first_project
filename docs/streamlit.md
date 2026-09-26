# Streamlit Dashboard Testing

## Environment

- Frontend: Streamlit
- Backend: FastAPI
- Model: XGBoost
- API: http://127.0.0.1:8000

---

## Functional Tests

### Test 1 — Application Startup

Expected:
- Streamlit starts successfully
- Dashboard loads
- No Python errors

Status: PASS

---

### Test 2 — API Health

Expected:
- Sidebar displays API Online
- `/health` returns HTTP 200

Status: PASS

---

### Test 3 — Valid Prediction

Expected:
- Prediction request succeeds
- Churn probability appears
- Prediction appears
- Risk level appears

Status: PASS

---

### Test 4 — Probability Gauge

Expected:
- Gauge appears
- Probability is between 0% and 100%

Status: PASS

---

### Test 5 — Churn vs Stay Chart

Expected:
- Stay probability appears
- Churn probability appears
- Both values are between 0% and 100%

Status: PASS

---

### Test 6 — Prediction History

Expected:
- Successful prediction is added
- Multiple predictions are displayed

Status: PASS

---

### Test 7 — Clear History

Expected:
- History is removed
- "No predictions have been made yet" appears

Status: PASS

---

### Test 8 — API Offline

Expected:
- API Offline message appears
- Prediction request shows connection error
- Streamlit does not crash

Status: PASS

---

### Test 9 — API Recovery

Expected:
- FastAPI restarted
- Streamlit reconnects
- Predictions work again

Status: PASS

---

## Final Result

Streamlit dashboard testing completed successfully.e