# Model Explainability

## Objective

Understand which features influence model predictions
and provide both global and local explanations.

## Model

XGBoost tuned model.

## Global Feature Importance

Document the top features from native XGBoost feature importance.

## Permutation Importance

Document the top original input features according to
permutation importance.

## SHAP Analysis

Document the most influential features according to SHAP.

## Global Interpretation

Describe general patterns observed in the model.

## Local Interpretation

Analyze at least one individual customer's prediction.

## Business Interpretation

Translate model contributions into understandable
customer-risk information.

## Important Distinction

Feature contribution represents model behavior and does
not establish causation.

## Limitations

- Correlated features
- One-hot encoded categorical variables
- Dataset limitations
- Model-specific explanations
- Explainability does not establish causal relationships

## work flow
             ML ENGINEERING
                  │
        ┌─────────┴─────────┐
        │                   │
     Modeling            Analysis
        │                   │
        ▼                   ▼
 Algorithms             EDA
        │               Evaluation
        ▼               Thresholds
 Tuning                  Explainability
        │
        ▼
     Pipeline
        │
        ▼
   Production