**Preprocessing details to the BADS_WS1920_known.csv (Training dataset).**

The following details are subject to change based on improvements made to the python code called [Feature engineering.ipynb]() file.

Python row 11: 


imported the relevent libraries needed for preprocessing. 

**import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

Panda turns the raw text data into DataFrame which makes it easy to  clean.
StandardScaler, OneHotEncoder, ColumnTransformer, SimpleImputer, and Pipeline are scikit-learn tools for scaling, encoding, imputing, and organizing preprocessing steps.

missing_by_column = df.isna().sum() used to counts missing values separately for every column to help decide whether to remove rows, fill missing values or use another treatment before modelling dataset.

Python row 12:

Created a list called date_columns = [
    "order_date",
    "delivery_date",
    "user_dob",
    "user_reg_date"]

Contains variables with dates that need to be converted to standard Datetime format. Datetime values can be used in calculations and also makes it easier to identify missing values. While errors="coerce" turns values that cannot be parsed into NaT (“Not a Time”), pandas treats then as missing-date value.

pd.to_datetime() parses the values as dates.

Python row 13:

I started off by printing the column’s data type, first five values, and count of missing or invalid dates using code: 
for column in date_columns:
    df[column] = pd.to_datetime(df[column], errors="coerce")

    print(f"\n{column}:")
    print("Data type:", df[column].dtype)
    print("Sample values:")
    print(df[column].head())
    print("Missing/invalid dates:", df[column].isna().sum())
It converts values to pandas datetime format and unparseable values to NaT translated by pandas as missing-date value.
























.
