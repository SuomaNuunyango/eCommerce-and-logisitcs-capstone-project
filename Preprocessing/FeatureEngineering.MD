**Feature engineering details to the BADS_WS1920_known.csv (Training dataset).**

The following details are subject to change based on improvements made to the python code called [Feature engineering.ipynb](https://github.com/SuomaNuunyango/eCommerce-and-logisitcs-capstone-project/blob/main/Preprocessing/Feature%20engineering.ipynb) file.

Python row 11: 

imported the relevent libraries needed for preprocessing. 

**import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

Panda turns the raw text data into DataFrame which makes it easy to  clean.
StandardScaler, OneHotEncoder, ColumnTransformer, SimpleImputer and Pipeline are scikit-learn tools for scaling, encoding, imputing and organizing preprocessing steps.

Code missing_by_column = df.isna().sum() is used to count missing values separately for every column to help decide whether to remove rows, fill missing values or use another treatment before modelling dataset later.

Python row 12:

Created a list called date_columns = [
    "order_date",
    "delivery_date",
    "user_dob",
    "user_reg_date"]

Contains variables with dates that need to be converted to standard Datetime format. Datetime values can be used in calculations and also makes it easier to identify missing values. 

While errors="coerce" turns values that cannot be parsed into NaT (“Not a Time”), whereby pandas treats then as missing-date value.

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

This is to ensure I get to see the columns will invalid or missing values so that I can test which method is best to fill the cells and fill with appropriate data using the correct method.

To converts values to pandas datetime format and unparseable values to NaT translated by pandas as missing-date value, I included df[column] = pd.to_datetime(df[column], errors="coerce" in the code to point out those cells.

Created new name called valid_delivery to calculate the days it takes to delivery orders using code: valid_delivery = df["delivery_date"].notna() & df["order_date"].notna().

valid_delivery = df["delivery_date"].notna() & df["order_date"].notna() looks through the DataFrame (df) and finds all rows with values for both order_date and the delivery_date. It filters out incomplete data. 

I calcuated the median for delivery_days using code: median_delivery_days = ((df.loc[valid_delivery, "delivery_date"] - df.loc[valid_delivery, "order_date"]).dt.days.median()). 

.dt.days converts that duration into a clean whole number of days, while .median() finds the middle value (median) of all missing/ invalid delivery days.

Then all missing (Blank) cells are filled with median in the delivery_day column using if pd.notna(median_delivery_days):
    missing_delivery = df["delivery_date"].isna() & df["order_date"].notna()
    df.loc[missing_delivery, "delivery_date"] = (df.loc[missing_delivery, "order_date"] + pd.to_timedelta(median_delivery_days, unit="D"))

Imputation was initially used to test if its the appropriate measure to fill the  missing values, which is later changed once a better method seeming appropriate is indetified.

Customer_age_years uses todays date and user_dob to test the viability of using this method to get the best age calculation.

Code df["customer_age_years"] = (today.year - dob.dt.year - birthday_not_yet_reached.astype("Int64")).astype("Int64") creates an integer age column based on the date of birth and today’s date. Missing birth dates remain missing.

Only delivery_date is imputed. user_dob is not filled; it is used to calculate age where possible to test if this statistical method is suiting for prediction.

Python row 14:

Recalculating customer_age_years using customer’s birth date and the order date, expressed approximately in years. Using the order date gives age at the time of the transaction, rather than age today using code: df["customer_age_years"] = (
    (df["order_date"] - df["user_dob"]).dt.days / 365.25)

Changed the code to df.loc[
    ~df["customer_age_years"].between(18, 150),
    "customer_age_years"] = pd.NA
df["customer_age_missing"] = df["customer_age_years"].isna().astype(int)
This is to include missing values when age is outside 18-150 years by using 1 when age is missing or invalid, and 0 otherwise.

Because I noticed missing values in delivery_days are caused by negative values by subtracting delivery_dates and ordder_dates when delivery dates come before order dates. I adjusted the code to filter out the missing values: df["delivery_days"] = (df["delivery_date"] - df["order_date"]).dt.days and df.loc[df["delivery_days"] < 0, "delivery_days"] = pd.NA.

Named a new features called  delivery_method, delivery_status and insurance_status. They contain inferred labels to help minimise the columns by dimensionalisation to reduce the features not needed for model training.

delivery_status labels and code include: status_by_method = {
    "Road": "slight damage",
    "Flight": "no damage",
    "Shipping": "minor damage"}
df["Delivery_status"] = df["Delivery_method"].map(status_by_method)

The code assumes a relationship between delivery method and damage without actual source. The aim is to find a relationship between delivery method and damage for every return. 

Delivery_method labels and codes include: df["Delivery_method"] = pd.NA
df.loc[df["delivery_days"] < 7, "Delivery_method"] = "Flight"
df.loc[df["delivery_days"].between(7, 13), "Delivery_method"] = "Road"
df.loc[df["delivery_days"] >= 14, "Delivery_method"] = "Shipping"

The aim is to find a relationship between delivery days and delivery mode for every return. 

Insurance_status labels and code include:df["Insurance_status"] = "not insured"
insured_condition = ((df["item_price"] > 50)& (df["Delivery_method"].isin(["Flight", "Shipping"])))
df.loc[insured_condition, "Insurance_status"] = "insured"

The aim is to find a relationship between delivery method and item prices for every return. 

To check and inspect these columns: customer_age_years, customer_age_missing, delivery_days, Delivery_method, Delivery_status, and Insurance_status, I used value_counts(dropna=False) includes missing values in the category counts. describe() gives statistics such as count, mean, standard deviation, minimum and quartiles for numeric columns.

Finally, it prints the first ten rows of the derived columns for a quick inspection.

Python row 15:

I performed a data quality check on delivery_date and order_date to determine the actual cause of missing and invalid values in the new feature delivery_days.

Code df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
df["delivery_date"] = pd.to_datetime(df["delivery_date"], errors="coerce")
Converts order_date and delivery_date to datetime values. Unparseable dates become NaT.
Calculates delivery_days as delivery date minus order date.
Creates masks to identify:
Missing: either date is missing/invalid, or the calculated duration is missing.
Negative: delivery occurred before the order date.

Code negative_mask = df["delivery_days"].lt(0) marks rows where delivery appears before the order date.

Prints the row counts, the percentage of rows with negative durations, and the mean of the negative durations.
Displays up to 20 rows with missing or invalid durations, showing only available columns from the requested list.

Python row 16: 




















.
