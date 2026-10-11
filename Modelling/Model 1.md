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
    
TASKS

1. Path handles file paths

2. joblib saves the trained model

3. scikit-learn provides Logistic Regression and the pipeline. 

4. model_utils handle data loading, preprocessing, evaluation and the random seed.

Loaded clean dataset using load_model_data() function
After loadning the cleaned dataset from feature engineering, I Created an artifacts folder for the saved model. parents=True creates any missing parent folders (exist_ok=True avoids an error if the folder already exists).

Pipeline() function chains preprocessing and classification together. This helps ensure the same preprocessing is applied during training and later predictions.

Logistic Regression hyperparameter settings:

1. C=1.0: Sets the strength of regularization (smaller values apply stronger regularization).

2. penalty="l2" Using L2 regularization to discourage overly large coefficients.

3. solver="liblinear": liblinear is the Optimization method that works well for many smaller binary-classification problems.

4. class_weight="balanced": Adjusts weights to account for class imbalance.

5. max_iter=2000: Allows more iterations for the solver to converge.

6. random_state=RANDOM_STATE: Makes results more reproducible where randomness is involved.

The following functions helped with the following capacilities:

model.fit(): Learns the preprocessing steps and model parameters using only the training data.

report_results(): Evaluates predictions on the test set. 

joblib.dump(): Saves the complete fitted pipeline—including preprocessing and classifier—to 
artifacts/logistic_regression_pipeline.joblib. 


X_train, X_test, y_train, y_test = load_model_data() loads the CSV file and returns features (X) and target labels (y) by splitting dataset into training and test sets. 


Python row 5:

code was used for:
output_dir = Path(".")
output_dir.mkdir(parents=True, exist_ok=True)
Path(".") means the is a working directory for the notebook if not the mkdir line ensures the folder exists by creating one if it doesn't exist. 

code:
X_subtrain, X_val, y_subtrain, y_val = train_test_split(
    X_train,
    y_train,
    test_size=0.2,
    random_state=RANDOM_STATE,
    stratify=y_train,)
    
used for dividing the original training set again:

80% (X_subtrain, y_subtrain) is used to train models at different sizes.

20% (X_val, y_val) is used to measure validation error.

stratify=y_train helps preserve the target-class proportions so that the test set is kept aside for final evaluation.

fractions = np.linspace(0.1, 1.0, 10). This creates 10 fractions from 10% to 100%. The loop will train a separate model using each fraction of the subtraining data.


These lists store the number of training rows and the two error measurements for the model.
sample_sizes = []

training_errors = []

validation_errors = []

For each fraction, the code calculates how many rows to use so that it ensures the sample has at least two rows and does not exceed the available data using this code n = max(2, int(len(X_subtrain) * fraction))
n = min(n, len(X_subtrain)).

This code then helps calculate classification error on both datasets:

zero_one_loss(y_part, curve_model.predict(X_part))
zero_one_loss(y_val, curve_model.predict(X_val))

Because output_dir is ".", it is saved in the current working directory. plt.show() displays the chart, and the final print reports the full resolved save path


