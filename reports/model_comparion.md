# Model Comparison

## Models Evaluated

1. Logistic Regression
2. Random Forest
3. XGBoost

## Evaluation Strategy

- Same train/test split
- Stratified split
- 5-fold Stratified Cross-Validation
- Metrics:
  - Accuracy
  - Precision
  - Recall
  - F1
  - ROC-AUC
  - PR-AUC

## Test Results

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC | PR-AUC |
|---|---:|---:|---:|---:|---:|---:|
| Logistic Regression | | | | | | |
| Random Forest | | | | | | |
| XGBoost | | | | | | |

## Cross-Validation Results

| Model | F1 Mean | F1 Std | ROC-AUC Mean | ROC-AUC Std |
|---|---:|---:|---:|---:|
| Logistic Regression | | | | |
| Random Forest | | | | |
| XGBoost | | | | |

## Observations

### Logistic Regression
- 

### Random Forest
- 

### XGBoost
- 

## Feature Importance

Important features identified by tree-based models:
- 
- 
- 

## Work Flow
Dummy
  │
  │ establishes minimum benchmark
  ↓
Logistic Regression
  │
  │ linear relationships
  ↓
Random Forest
  │
  │ nonlinear + ensemble
  ↓
XGBoost
  │
  │ sequential boosting
  ↓
Compare
  │
  ├── Test metrics
  ├── Cross-validation
  ├── Confusion matrices
  ├── ROC-AUC
  ├── PR-AUC
  └── Feature importance
  ↓
Candidate models