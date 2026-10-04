**Feature engineering details to the BADS_WS1920_known.csv (Training dataset).**

The following details are subject to change based on improvements made to the python code called [Feature engineering.;]() file.

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

I started off by printing the column’s data type, first five values and count of missing or invalid dates using code: 
for column in date_columns:
    df[column] = pd.to_datetime(df[column], errors="coerce")

    print(f"\n{column}:")
    print("Data type:", df[column].dtype)
    print("Sample values:")
    print(df[column].head())
    print("Missing/invalid dates:", df[column].isna().sum())

to converts values to pandas datetime format and unparseable values to NaT translated by pandas as missing-date value I included df[column] = pd.to_datetime(df[column], errors="coerce" in the code.

Created new name for delivery_days calucation using code: valid_delivery = df["delivery_date"].notna() & df["order_date"].notna().

valid_delivery = df["delivery_date"].notna() & df["order_date"].notna() looks through the DataFrame (df) and finds all rows with values for both order_date and the delivery_date. It filters out incomplete data. 

I calcuated the median for delivery_days using code: median_delivery_days = ((df.loc[valid_delivery, "delivery_date"] - df.loc[valid_delivery, "order_date"]).dt.days.median()). 
.dt.days converts that duration into a clean whole number of days.
.median() finds the middle value (median) of all delivery days.

Then all missing (Blank) cells are filled with median in the delivery_day column using if pd.notna(median_delivery_days):
    missing_delivery = df["delivery_date"].isna() & df["order_date"].notna()
    df.loc[missing_delivery, "delivery_date"] = (
        df.loc[missing_delivery, "order_date"]
        + pd.to_timedelta(median_delivery_days, unit="D"))

Code df.loc[...] specifically takes the order_date and adds the median_delivery_days to it (converted into a pandas time format using pd.to_timedelta).

Customer_age_years uses todays date and user_dob. Each time the code is run, clients age changes to get their current age. Because User_dob contains 8725 missing values to avoid creating more invalid data cells I avoided using order_date to get a much more current prediction.

Code df["customer_age_years"] = (today.year - dob.dt.year - birthday_not_yet_reached.astype("Int64")).astype("Int64") creates an integer age column based on the date of birth and today’s date. Missing birth dates remain missing.

Only delivery_date is imputed. user_dob is not filled; it is used to calculate age where possible.























.
