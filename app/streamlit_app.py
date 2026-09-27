import os
import requests
import streamlit as st
import plotly.graph_objects as go


API_URL = os.getenv(
    "API_URL",
    "http://127.0.0.1:8000"
)
# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Customer Churn Intelligence",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CONFIGURATION
# ============================================================

API_URL = "http://127.0.0.1:8000"


# ============================================================
# SESSION STATE
# ============================================================

if "prediction_history" not in st.session_state:
    st.session_state.prediction_history = []


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* Main page */

    .main {
        padding-top: 1rem;
    }


    /* Dashboard title */

    .dashboard-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }


    .dashboard-subtitle {
        font-size: 18px;
        opacity: 0.75;
        margin-bottom: 25px;
    }


    /* Section titles */

    .section-title {
        font-size: 24px;
        font-weight: 650;
        margin-top: 10px;
        margin-bottom: 15px;
    }


    /* Information cards */

    .info-card {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid rgba(128, 128, 128, 0.25);
        margin-bottom: 15px;
    }


    /* Prediction result card */

    .prediction-card {
        padding: 25px;
        border-radius: 15px;
        border: 1px solid rgba(128, 128, 128, 0.25);
        text-align: center;
        margin-top: 15px;
        margin-bottom: 20px;
    }


    .prediction-probability {
        font-size: 48px;
        font-weight: 700;
        margin-bottom: 5px;
    }


    .prediction-label {
        font-size: 17px;
        opacity: 0.7;
    }


    /* Risk cards */

    .risk-high {
        padding: 18px;
        border-radius: 12px;
        text-align: center;
        font-weight: 600;
        border: 1px solid rgba(220, 53, 69, 0.4);
    }


    .risk-medium {
        padding: 18px;
        border-radius: 12px;
        text-align: center;
        font-weight: 600;
        border: 1px solid rgba(255, 193, 7, 0.5);
    }


    .risk-low {
        padding: 18px;
        border-radius: 12px;
        text-align: center;
        font-weight: 600;
        border: 1px solid rgba(25, 135, 84, 0.4);
    }


    /* Footer */

    .footer {
        text-align: center;
        opacity: 0.6;
        padding: 20px;
        font-size: 13px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="dashboard-title">
        📊 Customer Churn Intelligence
    </div>

    <div class="dashboard-subtitle">
        Predict customer churn probability and identify customers
        who may require retention attention.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("⚙️ System")

    # --------------------------------------------------------
    # API STATUS
    # --------------------------------------------------------

    st.markdown("### API Status")

    try:

        health_response = requests.get(
            f"{API_URL}/health",
            timeout=5
        )

        if health_response.status_code == 200:

            st.success("🟢 API Online")

        else:

            st.error("🔴 API Error")

    except requests.exceptions.RequestException:

        st.error("🔴 API Offline")

        st.caption(
            "Start FastAPI before using predictions."
        )


    st.divider()


    # --------------------------------------------------------
    # MODEL INFORMATION
    # --------------------------------------------------------

    st.markdown("### 🤖 Model Information")

    st.info(
        """
        **Model:** XGBoost

        **Version:** Tuned

        **Task:** Binary Classification

        **Target:** Customer Churn

        **Prediction Threshold:** 0.50

        **Risk Thresholds:**

        - Low: < 0.40
        - Medium: 0.40 – 0.69
        - High: ≥ 0.70
        """
    )


    st.divider()

    st.caption(
        "Customer Churn Prediction System"
    )


# ============================================================
# CUSTOMER PROFILE
# ============================================================

st.markdown(
    '<div class="section-title">👤 Customer Profile</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)


# ------------------------------------------------------------
# PERSONAL INFORMATION
# ------------------------------------------------------------

with col1:

    st.markdown("#### Personal Information")

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    senior_citizen = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

    partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

    tenure = st.number_input(
        "Tenure (months)",
        min_value=0,
        max_value=100,
        value=5
    )


# ------------------------------------------------------------
# PHONE & INTERNET
# ------------------------------------------------------------

with col2:

    st.markdown("#### Phone & Internet")

    phone_service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    multiple_lines = st.selectbox(
        "Multiple Lines",
        ["Yes", "No", "No phone service"]
    )

    internet_service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

    online_security = st.selectbox(
        "Online Security",
        ["Yes", "No", "No internet service"]
    )

    online_backup = st.selectbox(
        "Online Backup",
        ["Yes", "No", "No internet service"]
    )


# ------------------------------------------------------------
# ADDITIONAL SERVICES
# ------------------------------------------------------------

with col3:

    st.markdown("#### Additional Services")

    device_protection = st.selectbox(
        "Device Protection",
        ["Yes", "No", "No internet service"]
    )

    tech_support = st.selectbox(
        "Tech Support",
        ["Yes", "No", "No internet service"]
    )

    streaming_tv = st.selectbox(
        "Streaming TV",
        ["Yes", "No", "No internet service"]
    )

    streaming_movies = st.selectbox(
        "Streaming Movies",
        ["Yes", "No", "No internet service"]
    )


# ============================================================
# BILLING & CONTRACT
# ============================================================

st.divider()

st.markdown(
    '<div class="section-title">💳 Billing & Contract</div>',
    unsafe_allow_html=True
)

billing_col1, billing_col2, billing_col3 = st.columns(3)


with billing_col1:

    contract = st.selectbox(
        "Contract",
        [
            "Month-to-month",
            "One year",
            "Two year"
        ]
    )


with billing_col2:

    paperless_billing = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )


with billing_col3:

    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )


# ============================================================
# FINANCIAL INFORMATION
# ============================================================

st.divider()

st.markdown(
    '<div class="section-title">💰 Financial Information</div>',
    unsafe_allow_html=True
)

financial_col1, financial_col2 = st.columns(2)


with financial_col1:

    monthly_charges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=80.5,
        step=1.0
    )


with financial_col2:

    total_charges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=400.5,
        step=1.0
    )


# ============================================================
# CUSTOMER DATA
# ============================================================

customer_data = {
    "gender": gender,
    "SeniorCitizen": senior_citizen,
    "Partner": partner,
    "Dependents": dependents,
    "tenure": tenure,
    "PhoneService": phone_service,
    "MultipleLines": multiple_lines,
    "InternetService": internet_service,
    "OnlineSecurity": online_security,
    "OnlineBackup": online_backup,
    "DeviceProtection": device_protection,
    "TechSupport": tech_support,
    "StreamingTV": streaming_tv,
    "StreamingMovies": streaming_movies,
    "Contract": contract,
    "PaperlessBilling": paperless_billing,
    "PaymentMethod": payment_method,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges
}


# ============================================================
# PREDICTION BUTTON
# ============================================================

st.divider()

button_col1, button_col2, button_col3 = st.columns(
    [1, 2, 1]
)

with button_col2:

    predict_button = st.button(
        "🔍 Predict Customer Churn",
        type="primary",
        use_container_width=True
    )


# ============================================================
# PREDICTION
# ============================================================

if predict_button:

    try:

        response = requests.post(
            f"{API_URL}/predict",
            json=customer_data,
            timeout=10
        )


        # ====================================================
        # SUCCESS
        # ====================================================

        if response.status_code == 200:

            result = response.json()

            probability = float(
                result["churn_probability"]
            )

            prediction = result["prediction"]

            risk_level = result["risk_level"]


            # =================================================
            # SAVE HISTORY
            # =================================================

            st.session_state.prediction_history.append(
                {
                    "Churn Probability": probability,
                    "Prediction": prediction,
                    "Risk Level": risk_level
                }
            )


            # =================================================
            # RESULT
            # =================================================

            st.divider()

            st.markdown(
                '<div class="section-title">📈 Prediction Result</div>',
                unsafe_allow_html=True
            )


            # =================================================
            # MAIN PREDICTION CARD
            # =================================================

            prediction_text = (
                "Likely to Churn"
                if prediction == "Yes"
                else "Likely to Stay"
            )

            st.markdown(
                f"""
                <div class="prediction-card">

                    <div class="prediction-probability">
                        {probability * 100:.2f}%
                    </div>

                    <div class="prediction-label">
                        Churn Probability
                    </div>

                    <br>

                    <strong>
                        {prediction_text}
                    </strong>

                </div>
                """,
                unsafe_allow_html=True
            )


            # =================================================
            # METRICS
            # =================================================

            metric1, metric2, metric3 = st.columns(3)


            with metric1:

                st.metric(
                    "Churn Probability",
                    f"{probability * 100:.2f}%"
                )


            with metric2:

                st.metric(
                    "Prediction",
                    prediction_text
                )


            with metric3:

                st.metric(
                    "Risk Level",
                    risk_level
                )


            # =================================================
            # PROBABILITY GAUGE
            # =================================================

            st.markdown(
                "### 🎯 Churn Probability"
            )

            gauge = go.Figure(
                go.Indicator(
                    mode="gauge+number",
                    value=probability * 100,
                    number={
                        "suffix": "%"
                    },
                    title={
                        "text": "Predicted Churn Probability"
                    },
                    gauge={
                        "axis": {
                            "range": [0, 100]
                        },
                        "bar": {
                            "thickness": 0.7
                        },
                        "steps": [
                            {
                                "range": [0, 40],
                                "color": "lightgreen"
                            },
                            {
                                "range": [40, 70],
                                "color": "lightyellow"
                            },
                            {
                                "range": [70, 100],
                                "color": "lightcoral"
                            }
                        ]
                    }
                )
            )

            gauge.update_layout(
                height=350,
                margin={
                    "l": 30,
                    "r": 30,
                    "t": 60,
                    "b": 20
                }
            )

            st.plotly_chart(
                gauge,
                use_container_width=True
            )


            # =================================================
            # CHURN VS STAY
            # =================================================

            st.markdown(
                "### 📊 Churn vs Stay"
            )

            stay_probability = 1 - probability

            chart = go.Figure(
                data=[
                    go.Bar(
                        x=[
                            "Stay",
                            "Churn"
                        ],
                        y=[
                            stay_probability * 100,
                            probability * 100
                        ],
                        text=[
                            f"{stay_probability * 100:.2f}%",
                            f"{probability * 100:.2f}%"
                        ],
                        textposition="auto"
                    )
                ]
            )

            chart.update_layout(
                yaxis_title="Probability (%)",
                yaxis={
                    "range": [0, 100]
                },
                height=400
            )

            st.plotly_chart(
                chart,
                use_container_width=True
            )


            # =================================================
            # RISK MESSAGE
            # =================================================

            if risk_level == "High":

                st.markdown(
                    """
                    <div class="risk-high">
                        🔴 HIGH RISK<br>
                        This customer has a high predicted
                        churn probability.
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            elif risk_level == "Medium":

                st.markdown(
                    """
                    <div class="risk-medium">
                        🟠 MEDIUM RISK<br>
                        This customer has a moderate predicted
                        churn probability.
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.markdown(
                    """
                    <div class="risk-low">
                        🟢 LOW RISK<br>
                        This customer has a relatively low
                        predicted churn probability.
                    </div>
                    """,
                    unsafe_allow_html=True
                )


        # ====================================================
        # API ERROR
        # ====================================================

        else:

            st.error(
                f"Prediction failed. "
                f"API returned status code "
                f"{response.status_code}."
            )

            try:

                error_detail = response.json()

                st.code(error_detail)

            except ValueError:

                st.write(response.text)


    # ========================================================
    # CONNECTION ERROR
    # ========================================================

    except requests.exceptions.ConnectionError:

        st.error(
            "🔴 Could not connect to the FastAPI server."
        )

        st.info(
            """
            Start FastAPI using:

            `uvicorn app.main:app --reload --reload-dir app`
            """
        )


    # ========================================================
    # TIMEOUT ERROR
    # ========================================================

    except requests.exceptions.Timeout:

        st.error(
            "⏱️ The API request timed out."
        )


    # ========================================================
    # REQUEST ERROR
    # ========================================================

    except requests.exceptions.RequestException as e:

        st.error(
            f"API request failed: {e}"
        )


    # ========================================================
    # UNEXPECTED ERROR
    # ========================================================

    except Exception as e:

        st.error(
            f"An unexpected error occurred: {e}"
        )


# ============================================================
# PREDICTION HISTORY
# ============================================================

st.divider()

st.markdown(
    '<div class="section-title">🕘 Prediction History</div>',
    unsafe_allow_html=True
)


if st.session_state.prediction_history:

    history_data = []

    for index, item in enumerate(
        st.session_state.prediction_history,
        start=1
    ):

        history_data.append(
            {
                "#": index,

                "Churn Probability": (
                    f"{item['Churn Probability'] * 100:.2f}%"
                ),

                "Prediction": (
                    "Likely to Churn"
                    if item["Prediction"] == "Yes"
                    else "Likely to Stay"
                ),

                "Risk Level": item["Risk Level"]
            }
        )


    st.table(history_data)


    if st.button(
        "🗑️ Clear Prediction History"
    ):

        st.session_state.prediction_history = []

        st.rerun()


else:

    st.info(
        "No predictions have been made yet."
    )


# ============================================================
# MODEL INFORMATION
# ============================================================

st.divider()

st.markdown(
    '<div class="section-title">🤖 Model Information</div>',
    unsafe_allow_html=True
)

model_col1, model_col2, model_col3, model_col4 = st.columns(4)


with model_col1:

    st.metric(
        "Model",
        "XGBoost"
    )


with model_col2:

    st.metric(
        "Model Version",
        "Tuned"
    )


with model_col3:

    st.metric(
        "Task",
        "Binary Classification"
    )


with model_col4:

    st.metric(
        "Threshold",
        "0.50"
    )


st.caption(
    "The model predicts the probability that a customer will "
    "churn. The prediction label is determined using a "
    "0.50 probability threshold."
)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        Customer Churn Prediction System
        • Machine Learning Engineering Project
    </div>
    """,
    unsafe_allow_html=True
)