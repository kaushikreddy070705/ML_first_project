# Hyperparameter Tuning

## Objective

Improve model generalization through systematic
hyperparameter search using cross-validation.

## Models Tuned

- Logistic Regression
- Random Forest
- XGBoost

## Validation Strategy

- Stratified 5-fold cross-validation
- Training set only
- Test set kept untouched during tuning

## Primary Search Metric

F1-score

## Random Forest Best Parameters

Paste actual parameters here.

## Random Forest Best CV Score

Paste actual score here.

## XGBoost Best Parameters

Paste actual parameters here.

## XGBoost Best CV Score

Paste actual score here.

## Test Set Evaluation

Paste actual final evaluation results here.

## Observations

- Did tuning improve F1?
- Did ROC-AUC improve?
- Did PR-AUC improve?
- Did recall change?
- Is there evidence of overfitting?
- How stable were CV results?

## Important Note

Hyperparameter tuning was performed only on the
training data using cross-validation. The test set
was reserved for final evaluation.

## work flow

                 RAW DATA
                    │
                    ▼
             Train/Test Split
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
       TRAIN                 TEST
          │                   │
          ▼                   │
    Cross Validation          │
          │                   │
          ▼                   │
 Hyperparameter Search        │
          │                   │
          ▼                   │
   Best Configuration         │
          │                   │
          ▼                   │
   Train Best Model           │
          │                   │
          └─────────┐         │
                    ▼         ▼
                FINAL TEST EVALUATION