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

Setting the target feature apart I used code:

target_column = "return".
df = df.dropna(subset=[target_column])

Set "return" as the outcome to predict, then remove rows where that outcome is missing. The model needs a known answer for each training.

**Splits the data into:**

80% training data (X_train, y_train) for fitting the model.
20% test data (X_test, y_test) for evaluating it on data it has not trained on.

random_state=RANDOM_STATE makes the split reproducible by setting it to default of 42.

stratify=y keeps the proportion of returns and non-returns roughly similar in both sets














OneHotEncoder — Converts categorical values, such as product type or delivery method, into numeric features a model can use.
ColumnTransformer — Applies different preprocessing steps to different columns, such as imputing numeric columns and encoding categorical ones.
