Python row 3:

Importing relevent libraries: 
from pathlib import Path
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from model_utils import (
    load_model_data,
    make_preprocessor,
    report_results,
    RANDOM_STATE,)
    

Path handles file paths

joblib saves the trained model

scikit-learn provides Logistic Regression and the pipeline. 

model_utils handle data loading, preprocessing, evaluation and the random seed.

Loaded clean dataset using load_model_data() function
After loadning the cleaned dataset from feature engineering, I Created an artifacts folder for the saved model. parents=True creates any missing parent folders (exist_ok=True avoids an error if the folder already exists).

Pipeline() function chains preprocessing and classification together. This helps ensure the same preprocessing is applied during training and later predictions.

Logistic Regression hyperparameter settings:

C=1.0: Sets the strength of regularization (smaller values apply stronger regularization).

penalty="l2" Using L2 regularization to discourage overly large coefficients.

solver="liblinear": liblinear is the Optimization method that works well for many smaller binary-classification problems.

class_weight="balanced": Adjusts weights to account for class imbalance.

max_iter=2000: Allows more iterations for the solver to converge.

random_state=RANDOM_STATE: Makes results more reproducible where randomness is involved.

The following functions helped with the following capacilities:

model.fit(): Learns the preprocessing steps and model parameters using only the training data.

report_results(): Evaluates predictions on the test set. 

joblib.dump(): Saves the complete fitted pipeline—including preprocessing and classifier—to 
artifacts/logistic_regression_pipeline.joblib. 


X_train, X_test, y_train, y_test = load_model_data() loads the CSV file and returns features (X) and target labels (y) by splitting dataset into training and test sets. 






