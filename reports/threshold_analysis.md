# Threshold Analysis

## Objective

Evaluate model performance across different classification
thresholds and understand the precision-recall trade-off.

## Model Evaluated

XGBoost

## Default Threshold

0.50

## Metrics

- Accuracy
- Precision
- Recall
- F1
- ROC-AUC
- PR-AUC

## Confusion Matrix

Describe the TP, TN, FP and FN results.

## Threshold Analysis

Describe how precision, recall and F1 changed as the
threshold changed.

## Threshold Optimization

The threshold producing the highest F1 among the evaluated
threshold grid was identified for analytical purposes.

## Business Cost Analysis

A hypothetical cost model was used to demonstrate how
business assumptions can influence threshold selection.

These costs are illustrative and do not represent actual
telecom business economics.

## Calibration

Describe whether predicted probabilities appear well calibrated.

## Important Limitation

Threshold selection should ideally be performed using
validation or out-of-fold predictions, with the final
test set remaining untouched for unbiased evaluation.

## work flow
                    CUSTOMER CHURN PROJECT
                            │
                            ▼
                    Problem Definition
                            │
                            ▼
                       Data Collection
                            │
                            ▼
                           EDA
                            │
                            ▼
                  Cleaning & Preprocessing
                            │
                            ▼
                    Baseline Modeling
                            │
                            ▼
                    Model Comparison
                            │
                            ▼
                  Hyperparameter Tuning
                            │
                            ▼
              ┌─────────────────────────┐
              │ Model Evaluation        │
              │                         │
              │ Precision               │
              │ Recall                  │
              │ F1                      │
              │ ROC-AUC                 │
              │ PR-AUC                  │
              └────────────┬────────────┘
                           │
                           ▼
                 Threshold Analysis
                           │
                           ▼
                  Business Trade-offs
                           │
                           ▼
                    Final Model