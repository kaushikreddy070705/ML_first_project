# Baseline Model Results

## Models

### Dummy Classifier
Strategy:
- Most frequent class

Purpose:
- Establish minimum baseline

### Logistic Regression
Purpose:
- Establish first meaningful ML benchmark

## Metrics

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC | PR-AUC |
|---|---:|---:|---:|---:|---:|---:|
| Dummy | ... | ... | ... | ... | ... | ... |
| Logistic Regression | ... | ... | ... | ... | ... | ... |

## Cross Validation

5-fold Stratified Cross Validation was used for Logistic Regression.

## Observations

- [Write your observation]
- [Write your observation]
- [Write your observation]

## Limitations

The test set is reserved for final evaluation and should not be repeatedly used for model selection.

## Architecture
                    RAW DATA
                       │
                       ↓
              Data Preprocessing
                       │
                       ↓
              Train / Test Split
                       │
          ┌────────────┴────────────┐
          ↓                         ↓
      Dummy Model             Logistic Regression
          │                         │
          └────────────┬────────────┘
                       ↓
                  Predictions
                       │
                       ↓
              ┌────────┴─────────┐
              ↓                  ↓
          Class Labels       Probabilities
              │                  │
              ↓                  ↓
       Confusion Matrix    ROC / PR Curves
              │                  │
              └────────┬─────────┘
                       ↓
                  Evaluation
                       ↓
                Baseline Result