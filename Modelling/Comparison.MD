# Comparison of Model 1 and Model 2

## 1. Objective

This report compares:

- **Model 1:** Logistic Regression — `Model 1 (Logistical Regression)(1).ipynb`
- **Model 2:** Random Forest — `Model 2 (Random Forest).ipynb`

Both models predict the binary `return` target (`0` = not returned; `1` = returned) using `cleaned_model_dataset.csv`.

Model 1 obtains its data split through `model_utils.py`, while Model 2 creates its split directly in its notebook. Confirm that both use the same 80/20 stratified split and same random seed before treating the test metrics as a direct head-to-head comparison.

## 2. Evaluation design and statistical methods

### Hold-out test evaluation

Both workflows use a hold-out test set to estimate performance on data not used for model fitting. A stratified 80/20 split is used in the supplied code or helper workflow. Stratification aims to preserve the proportion of returned and non-returned items in both partitions.

### Cross-validation for model selection

| Method | Model 1: Logistic Regression | Model 2: Random Forest |
|---|---|---|
| Search method | `GridSearchCV` | `RandomizedSearchCV` |
| Cross-validation | 5-fold CV | 3-fold stratified CV |
| Search size | 24 combinations | 6 sampled combinations |
| Selection metric | ROC-AUC | ROC-AUC |
| Main parameters tuned | `C`, `penalty`, `class_weight` | `n_estimators`, `max_depth`, `min_samples_leaf`, `max_features`, `class_weight` |

Cross-validation estimates how the candidate models perform across multiple training/validation partitions of the training data. ROC-AUC is used to select configurations because it assesses ranking ability across classification thresholds. Cross-validation scores should not be confused with final held-out test scores.

### Metrics used

- **Accuracy:** proportion of all cases classified correctly.
- **Precision:** proportion of predicted returns that are actual returns.
- **Recall (sensitivity):** proportion of actual returns detected.
- **F1-score:** harmonic mean of precision and recall.
- **ROC-AUC:** threshold-independent ranking/discrimination measure; 0.5 indicates chance-level ranking.
- **Confusion matrix:** counts of true negatives (TN), false positives (FP), false negatives (FN) and true positives (TP).
- **Classification report:** class-level precision, recall, F1-score and support.
- **Training/validation or training/test error curve:** plots classification error (`1 − accuracy`) against training-set size to help diagnose possible underfitting or overfitting.

These metrics describe different aspects of performance. For return prediction, recall may matter if missing a likely return is costly, while precision may matter if interventions on predicted returns are expensive. The metric to prioritise should reflect the operational goal.

## 3. Results comparison

| Metric | Model 1: Logistic Regression | Model 2: Random Forest | Better result (based on metric) |
|---|---:|---:|---|
| Best cross-validation ROC-AUC | **0.6062*** | **0.6649** | Random Forest |
| Test accuracy | **0.5780** | **0.6290** | Random Forest |
| Test precision (class 1) | **0.5373** | **0.5973** | Random Forest |
| Test recall (class 1) | **0.5698** | **0.5838** | Random Forest |
| Test F1-score (class 1) | **0.5531** | **0.5905** | Random Forest |
| Test ROC-AUC | **0.6088*** | **0.6844** | Random Forest |
| False positives (FP) | **4,497** | **3,607** | Random Forest (fewer false alarms) |
| False negatives (FN) | **3,942** | **3,814** | Random Forest (fewer missed returns) |


## 4. Interpretation framework

The Random Forest model performed better than Logistic Regression across all reported predictive metrics. It achieved higher cross-validation ROC-AUC (0.6649 vs. 0.6062) and test ROC-AUC (0.6844 vs. 0.6088), suggesting stronger ability to distinguish between returned and not-returned cases. It also had higher test accuracy, precision, recall, and F1-score.
The Random Forest produced fewer false positives (3,607 vs. 4,497) and fewer false negatives (3,814 vs. 3,942). This means it made fewer incorrect return predictions and missed fewer actual returns. However, both models’ scores indicate there is still substantial room for improvement. Training/test error curves were not provided, so their generalization behavior cannot be compared from the available results.

The comparison is based on the following two notebooks:

- `Model 1 (Logistical Regression)(1).ipynb`
- `Model 2 (Random Forest).ipynb`



