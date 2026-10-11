# Model 1 Performance: Logistic Regression

## 1. Overview

This report documents the performance evaluation of **Model 1- Logistic Regression**, for predicting whether an order item is returned. The target variable is `return`, where `0` represents not returned and `1` represents returned, as used by the model python code. The following links contain the datasets and python code file used to measure the models performance.

**Python notebook used:** [Model 1 (Logistical Regression)(1).ipynb](https://github.com/SuomaNuunyango/eCommerce-and-logisitcs-capstone-project/blob/main/Modelling/Model%201%20(Logistical%20Regression).ipynb)  
**Shared helper module:** [model_utils.py](https://github.com/SuomaNuunyango/eCommerce-and-logisitcs-capstone-project/blob/main/Modelling/model_utils.py)  
**Dataset used:** [cleaned_model_dataset.csv]()

## 2. Statistical methodology

### Data preparation and split

The python notebook includes loading the dataset through `load_model_data()` from `model_utils.py`. The model uses a stratified 80/20 training/test split with `RANDOM_STATE` supplied by the helper module. Stratification helps preserve the target-class proportions in each split. The held-out test set should be used for final evaluation, not for selecting hyperparameters.

### Preprocessing and model specification

The model is implemented as a scikit-learn `Pipeline`, so preprocessing and model fitting are connected in one workflow. The notebook calls `make_preprocessor(scale_numeric=True)`, then fits Logistic Regression with these settings:

| Parameter | Value |
|---|---|
| `C` | `1.0` |
| `penalty` | `l2` |
| `solver` | `liblinear` |
| `class_weight` | `balanced` |
| `max_iter` | `2000` |
| Random state | `RANDOM_STATE` from `model_utils.py` |

`C` controls the inverse strength of regularisation. L2 regularisation penalises large coefficients, while `class_weight="balanced"` adjusts class weights inversely to class frequency.

### Hyperparameter tuning and statistical validation

The notebook uses `GridSearchCV` to compare 24 combinations:

- `C`: `0.001`, `0.01`, `0.1`, `1.0`, `10.0`, `100.0`
- `penalty`: `l1`, `l2`
- `class_weight`: `None`, `balanced`

The search uses **5-fold cross-validation** and selects parameters by **ROC-AUC**. Each candidate is evaluated across five training/validation folds, and the mean cross-validation ROC-AUC is used to rank the candidates. The notebook records the best parameters and best mean cross-validation ROC-AUC.

The notebook also plots training and validation classification error against training-set size. Classification error is `1 − accuracy`; the gap between training and validation error can help diagnose if the model is underfitting or overfitting.

## 3. Performance metrics

### Logistic Regression — Held-Out Test Results

| Metric | Score |
|---|---:|
| Accuracy | 0.5780 |
| Precision | 0.5373 |
| Recall | 0.5698 |
| F1-score | 0.5531 |
| ROC-AUC | 0.6088 |

### Confusion Matrix

| Actual \ Predicted | Not returned (0) | Returned (1) |
|---|---:|---:|
| Not returned (0) | 6,339 | 4,497 |
| Returned (1) | 3,942 | 5,222 |

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Not returned (0) | 0.62 | 0.58 | 0.60 | 10,836 |
| Returned (1) | 0.54 | 0.57 | 0.55 | 9,164 |
| Accuracy | — | — | 0.58 | 20,000 |
| Macro average | 0.58 | 0.58 | 0.58 | 20,000 |
| Weighted average | 0.58 | 0.58 | 0.58 | 20,000 |



## 4. Results and interpretation

The notebook's recorded grid search selected `C=1.0`, `class_weight='balanced'`, and `penalty='l2'`, which matched the initial model settings. Its recorded mean cross-validation ROC-AUC was **0.6062**, compared with the recorded test ROC-AUC of **0.6088**.

These ROC-AUC values are only modestly above 0.5, which represents chance-level ranking. The close cross-validation and test ROC-AUC values suggest similar ranking performance across those evaluations, but they do **not** by themselves prove that the model generalises well or that the predictions are useful. Accuracy, precision, recall, F1-score and the confusion matrix should be reported alongside ROC-AUC.

Logistic Regression models a linear relationship between the input features and the target features. If the relationship between the engineered features and returns is more complex, this model may underfit. The error versus training-size plot should be reviewed to see whether training and validation errors remain high or diverge.


## 5. How to run

1. First access the following notebook and csv file, `model_utils.py`, and `cleaned_model_dataset.csv` to use for model training.
2. Update the python notebook file `Model 1 (Logistical Regression)(1).ipynb` with the link to your `data_path` values based on file's location on your computer.
3. Install the required dependencies using  `requirements.txt` in the modelling repository's.
4. Run the notebook from top to bottom by using `run all` to have the notebook run all cells.


The main performance calculation is in **`Model 1 (Logistical Regression)(1).ipynb`**. The helper functions are in **`model_utils.py`**.
