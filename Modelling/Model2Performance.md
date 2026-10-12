# Model 2 Performance: Random Forest

## 1. Overview

This report documents **Model 2, Random Forest**, for predicting whether an order item is returned. The code uses `return` as the target, with `0` representing not returned and `1` representing returned.

**Python notebook used:** [Model 2 (Random Forest).ipynb](https://github.com/SuomaNuunyango/eCommerce-and-logisitcs-capstone-project/blob/main/Modelling/Model%202%20(Random%20Forest).ipynb)  
**Shared helper module:** [model_utils.py](https://github.com/SuomaNuunyango/eCommerce-and-logisitcs-capstone-project/blob/main/Modelling/model_utils.py)  
**Dataset used:** [cleaned_model_dataset.csv](https://github.com/SuomaNuunyango/eCommerce-and-logisitcs-capstone-project/blob/main/Modelling/cleaned_model_dataset.csv)

## 2. Statistical methodology

### Data preparation and split

The notebook removes rows where the target `return` is missing, separates the target from the features, and uses a stratified 80/20 train/test split with `random_state=42`. The held-out test set is reserved for final evaluation.

Numeric columns are imputed with their median. Categorical columns are imputed with their most frequent value and one-hot encoded; `handle_unknown="ignore"` allows the encoder to handle categories that appear in test data but were not present during training. Preprocessing is included in a scikit-learn pipeline.

### Model specification

The notebook uses `RandomForestClassifier` with `random_state=42` and `n_jobs=2`. Random Forest combines predictions from multiple decision trees trained on bootstrapped samples and feature subsets. This can capture non-linear relationships and interactions between features.

### Hyperparameter tuning and statistical validation

The notebook uses `RandomizedSearchCV` with:

- **3-fold stratified cross-validation** (`StratifiedKFold`, shuffled, `random_state=42`)
- **6 sampled parameter combinations** (`n_iter=6`)
- **ROC-AUC** as the model-selection metric
- `refit=True`, so the best configuration is refitted on the full training set
- `random_state=42` for reproducible sampling of candidate settings

The search space is:

| Hyperparameter | Candidate values |
|---|---|
| `n_estimators` | `50`, `100`, `150` |
| `max_depth` | `10`, `20`, `None` |
| `min_samples_leaf` | `1`, `2`, `4` |
| `max_features` | `"sqrt"`, `0.5` |
| `class_weight` | `"balanced"`, `None` |

Randomized search samples six combinations from this space; it does **not** evaluate every possible combination. The selected model is then evaluated on the held-out test set.


## 3. Performance metrics

### Best Cross-Validation Result

| Metric | Score |
|---|---:|
| Best cross-validation ROC-AUC | 0.6649 |

### Best Parameters

| Parameter | Value |
|---|---:|
| `classifier__n_estimators` | 150 |
| `classifier__min_samples_leaf` | 1 |
| `classifier__max_features` | 0.5 |
| `classifier__max_depth` | 20 |
| `classifier__class_weight` | None |

### Held-Out Test Results

| Metric | Score |
|---|---:|
| Accuracy | 0.6290 |
| Precision | 0.5973 |
| Recall | 0.5838 |
| F1-score | 0.5905 |
| ROC-AUC | 0.6844 |

### Confusion Matrix

| Actual \ Predicted | Not returned (0) | Returned (1) |
|---|---:|---:|
| Not returned (0) | 7,229 | 3,607 |
| Returned (1) | 3,814 | 5,350 |

### Classification Report

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Not returned (0) | 0.65 | 0.67 | 0.66 | 10,836 |
| Returned (1) | 0.60 | 0.58 | 0.59 | 9,164 |
| Accuracy | — | — | 0.63 | 20,000 |
| Macro average | 0.63 | 0.63 | 0.63 | 20,000 |
| Weighted average | 0.63 | 0.63 | 0.63 | 20,000 |

## 4. Results and interpretation

The performance of the model is better then Logistic Regression, reaching an overall accuracy of 62.90%. What makes this model truly special is that it is much more balanced. 

• Accuracy: 62.90% (0.6290)
	• Out of the 20,000 hidden test cases, it got the answer right nearly 63% of the time. This is a step up from the tuned  from Logistic Regression (57.80%).
  
• ROC-AUC: 68.44% (0.6844)
	• The model’s ability to cleanly separate the "Returned" items from the "Not Returned" items has improved visibly, creeping closer to a reliable 70% baseline.

• Confusion matrix

  Out of the 20,000 test cases, here is exactly where this model succeeded and where it slipped up:

• Correct "Not Returned" (7,229): It successfully identified 7,229 cases of `0`.
  • False Alarms (3,607): It guessed `1` when the true answer was `0`. 
  • Missed Cases (3,814): It guessed `0` when the true answer was actually `1`. 
  • Correct "Returned" (5,350): It successfully caught 5,350 real cases of `1` (its highest count).

While an accuracy of 63% still means it makes plenty of mistakes, this algorithm handles the data much more effectively. Instead of being heavily biased toward one group, its balanced F1-scores (0.66 for Class 0 and 0.59 for Class 1) prove that it is putting up a much stronger, fairer fight across both outcomes


## 5. How to use the ipynb file

1. First access the following notebook and csv file, `model_utils.py`, and `cleaned_model_dataset.csv` to use for model training.
2. Update the python notebook file `Model 2 (Random Forest).ipynb` with the link to your `data_path` values based on file's location on your computer.


3. Install the required dependencies using  `requirements.txt` in the modelling repository's.
4. Run the notebook from top to bottom by using `run all` to have the notebook run all cells.
