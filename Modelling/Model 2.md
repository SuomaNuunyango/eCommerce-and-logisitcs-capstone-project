Modelling details to the BADS_WS1920_known.csv (Training dataset).

The following details are subject to change based on improvements made to the Python file called Model 2 ([Random Forest](https://github.com/SuomaNuunyango/eCommerce-and-logisitcs-capstone-project/blob/main/Modelling/Model%202%20(Random%20Forest).ipynb).ipynb.


Python row 1:

Loaded the cleaned dataset using code: 

import pandas as pd

df = pd.read_csv("/Users/augustenuunyango/data/cleaned_model_dataset.csv")

containing all new features.

from sklearn module i imported libraries that perform the needed task to preprocess the data features and split the datasets into training and testing the model on Random Forest for better classification of data through complex, interaction within the data.

* from sklearn.base import clone — Makes a fresh copy of an estimator (such as a model or pipeline), without carrying over its fitted state. Useful when reusing model configurations.
   
* RandomForestClassifier — Trains a model made of many decision trees to predict categories, such as whether an order will be returned.
  
* SimpleImputer — Fills in missing values, for example with the median for numeric columns or the most common value for categories.
  
* train_test_split — Splits data into training and test sets so you can evaluate the model on data it did not train on.

* RandomizedSearchCV — Tries randomly selected combinations of model settings and uses cross-validation to find promising ones.
  
* StratifiedKFold — Creates cross-validation folds while preserving roughly the same class proportions in each fold. Helpful when returns and non-returns are imbalanced.
  
* Pipeline — Chains preprocessing and model steps together, helping ensure the same transformations are applied consistently and preventing data leakage.

**Evaluation metrics include:**

accuracy_score — Fraction of all predictions that are correct.

precision_score — Of the orders predicted to be returned, the fraction that actually were.

recall_score — Of the orders that were actually returned, the fraction the model identified.

f1_score — A combined measure of precision and recall.

roc_auc_score — Measures how well the model ranks returned orders above non-returned orders across classification thresholds.

confusion_matrix — Counts correct and incorrect predictions by class.

classification_report — Summarizes precision, recall, and F1-score for each class

OneHotEncoder — Converts categorical values, such as product type or delivery method, into numeric features a model can use.

ColumnTransformer — Applies different preprocessing steps to different columns, such as imputing numeric columns and encoding categorical ones.



Setting the target feature apart I used code:

target_column = "return".
df = df.dropna(subset=[target_column])

Set "return" as the outcome to predict, then remove rows where that outcome is missing. The model needs a known answer for each training.

**Splits the data into:**

80% training data (X_train, y_train) for fitting the model.
20% test data (X_test, y_test) for evaluating it on data it has not trained on.

random_state=RANDOM_STATE makes the split reproducible by setting it to default of 42.

stratify=y keeps the proportion of returns and non-returns roughly similar in both sets



Prepossessed numerical and categorical features before training using:

Numeric columns: SimpleImputer(strategy="median") fills missing values with each column’s median.

Categorical columns: A Pipeline first fills missing values with the most common value, then OneHotEncoder turns categories into numeric indicator columns.

ColumnTransformer: Applies each set of steps only to the columns listed in numeric_columns or categorical_columns, then combines the results

scikit-learn pipeline preprocesses the data and then trains a random forest classifier. I selected a smaller sample for tuning, so that the model processes data faster during training. Code used was:

param_distributions = {
    "classifier__n_estimators": [50, 100, 150],
    "classifier__max_depth": [10, 20, None],
    "classifier__min_samples_leaf": [1, 2, 4],
    "classifier__max_features": ["sqrt", 0.5],
    "classifier__class_weight": ["balanced", None]}

param_distributions lists the hyperparameter values to try when tuning your pipeline—often with RandomizedSearchCV or GridSearchCV.

The classifier__ prefix means set this parameter on the pipeline step named classifier. The double underscore is how scikit-learn addresses parameters inside a pipeline.

n_estimators: [50, 100, 150] — number of decision trees in the forest.

max_depth: [10, 20, None] — maximum depth of each tree. None means trees can grow until other stopping rules prevent further growth.

min_samples_leaf: [1, 2, 4] — minimum number of training examples a leaf (a tree’s final prediction node) must contain. Larger values can make the model less prone to overfitting.

max_features: ["sqrt", 0.5] — how many features each tree considers when looking for a split. "sqrt" uses roughly the square root of the total features; 0.5 uses half.

class_weight: ["balanced", None] — whether to compensate for classes that appear unequally often. "balanced" gives more weight to less common classes; None treats classes equally

n_jobs=2 tells the random forest to use up to two CPU cores at the same time for work. This helps make training and prediction faster than using one core.

I used randomized hyperparameter search for the model- random forest. It tests several parameter combinations, evaluates each using cross-validation and keeps the best-performing one. Randomized search samples a chosen number instead of testing every possible combination.

test set is then tested on the model using code:

best_rf = search.best_estimator_
y_pred = best_rf.predict(X_test)
y_prob = best_rf.predict_proba(X_test)[:, 1]

search.best_estimator_ — the model refitted on the full training data using the best hyperparameters found during the search. This works because you set refit=True.

best_rf.predict(X_test) — predicts a class label for each test example, such as 0 or 1. The model uses its default decision threshold.

best_rf.predict_proba(X_test) — returns class probabilities for each test example. For binary classification, the result has two columns: probability of class 0 and probability of class 1.

[:, 1] — selects the second column, giving the probability of class 1 for every test example









          
            
            
          
          














