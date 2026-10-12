# Comparison of Model 1 and Model 2

## 1. Objective

This report compares:

- **Model 1:** Logistic Regression — `Model 1 (Logistical Regression)(1).ipynb`
- **Model 2:** Random Forest — `Model 2 (Random Forest).ipynb`

Both models predict the binary `return` target (`0` = not returned; `1` = returned) using `cleaned_model_dataset.csv`.

**Important:** A fair comparison requires the same dataset version, target definition, train/test rows, preprocessing rules where appropriate, and metric definitions. Model 1 obtains its data split through `model_utils.py`, while Model 2 creates its split directly in its notebook. Confirm that both use the same 80/20 stratified split and same random seed before treating the test metrics as a direct head-to-head comparison.

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

Fill in this table using the printed output from the current runs. Do not replace missing values with estimates or assume that one model is better before comparing the results.

| Metric | Model 1: Logistic Regression | Model 2: Random Forest | Better result (based on metric) |
|---|---:|---:|---|
| Best cross-validation ROC-AUC | **0.6062*** | **[Insert result]** | **[Compare]** |
| Test accuracy | **[Insert result]** | **[Insert result]** | **[Compare]** |
| Test precision (class 1) | **[Insert result]** | **[Insert result]** | **[Compare]** |
| Test recall (class 1) | **[Insert result]** | **[Insert result]** | **[Compare]** |
| Test F1-score (class 1) | **[Insert result]** | **[Insert result]** | **[Compare]** |
| Test ROC-AUC | **0.6088*** | **[Insert result]** | **[Compare]** |
| False positives (FP) | **[Insert count]** | **[Insert count]** | **[Interpret cost]** |
| False negatives (FN) | **[Insert count]** | **[Insert count]** | **[Interpret cost]** |
| Training/test error curve | **[Summarise curve]** | **[Summarise curve]** | **[Compare generalisation]** |

\* The supplied Logistic Regression notebook's markdown records a best cross-validation ROC-AUC of **0.6062** and test ROC-AUC of **0.6088**. Confirm these figures against the final dataset and code run before submission. The supplied Random Forest notebook has no saved outputs, so its numerical results must be filled in after execution.

### Confusion matrix comparison

Record the two confusion matrices, both in label order `[0, 1]`.

**Model 1 — Logistic Regression**

|  | Predicted 0 | Predicted 1 |
|---|---:|---:|
| Actual 0 | **[TN]** | **[FP]** |
| Actual 1 | **[FN]** | **[TP]** |

**Model 2 — Random Forest**

|  | Predicted 0 | Predicted 1 |
|---|---:|---:|
| Actual 0 | **[TN]** | **[FP]** |
| Actual 1 | **[FN]** | **[TP]** |

## 4. Interpretation framework

Use the actual metrics to complete the statements below:

1. **Overall classification:** Model **[1/2]** had higher test accuracy (**[value]**) compared with **[value]**. This indicates **[interpretation, with any class-imbalance caveat]**.
2. **Detecting returns:** Model **[1/2]** had higher recall (**[value]**), meaning it detected a larger proportion of returned items. This is important if false negatives are costly.
3. **Reliability of return alerts:** Model **[1/2]** had higher precision (**[value]**), meaning a larger proportion of its predicted returns were actually returned.
4. **Balance of precision and recall:** Model **[1/2]** had the higher F1-score (**[value]**), providing the stronger balance between these two measures for the positive class.
5. **Ranking ability:** Model **[1/2]** had higher test ROC-AUC (**[value]**). Compare this with each model's CV ROC-AUC to assess whether performance appears consistent between cross-validation and the hold-out set.
6. **Generalisation:** Based on the error curves, **[model]** shows **[small/large]** training-to-validation/test error gap. This is **[consistent/not clearly consistent]** with overfitting. Do not infer overfitting from training error alone.
7. **Final selection:** Choose Model **[1/2]** if the priority is **[metric/business objective]**, while noting **[trade-off or limitation]**.

## 5. Statistical significance and uncertainty

The supplied notebooks report point estimates and cross-validation scores; they do **not** currently calculate confidence intervals or conduct a formal statistical significance test between the two models. Therefore, do not describe a small metric difference as statistically significant.

For a stronger statistical comparison, evaluate both models on the exact same held-out test rows and consider paired bootstrap confidence intervals for differences in ROC-AUC, F1-score or accuracy. For a paired accuracy comparison, McNemar's test may be appropriate because the two classifiers predict the same test observations. These analyses should be added to the code and reported only after they have actually been calculated. A single train/test split and cross-validation means alone do not establish statistical significance.

## 6. Limitations and validity checks

- **Comparable split:** Model 1 uses `load_model_data()` from `model_utils.py`; Model 2 defines its split in its notebook. Verify identical test rows before making direct comparisons.
- **Target leakage:** Check that all features are available at the intended time of prediction and that no post-return information is included.
- **Threshold effects:** Precision, recall, F1 and confusion matrix depend on the classification threshold. ROC-AUC does not use a single threshold.
- **Class distribution:** Report the class counts or proportions in the dataset and test set; accuracy alone may be misleading when classes are imbalanced.
- **Reproducibility:** Record the dataset version, random seed, library versions, selected hyperparameters and date of the final run.
- **No invented results:** Populate all placeholders from the current notebook outputs.

## 7. Code and how to reproduce

The comparison is based on the following two notebooks:

- [`Model 1 (Logistical Regression)(1).ipynb`](Model%201%20(Logistical%20Regression)(1).ipynb)
- [`Model 2 (Random Forest).ipynb`](Model%202%20(Random%20Forest).ipynb)

To reproduce the results:

1. Ensure both notebooks use the same `cleaned_model_dataset.csv` and the same target definition.
2. Update the absolute dataset paths to work on your computer.
3. Ensure `model_utils.py` is available for Model 1.
4. Install the dependencies in `requirements.txt`.
5. Run both notebooks from top to bottom.
6. Copy the actual test metrics, CV scores, selected parameters and confusion matrices into this report.
7. Review the generated error curves and complete the interpretation statements using evidence from the results.

## 8. Conclusion

The final conclusion should name the stronger model for the metric that matters most to the returns problem, rather than simply choosing the model with the highest accuracy. State the measured differences, explain the trade-offs between false positives and false negatives, and acknowledge that formal statistical significance has not been tested unless the additional paired analysis is implemented.
