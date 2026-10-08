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

After converting date column to pandas datetime format, calculated the new feature customer_age_years by subtracting order_date from user_dob/ 365.25, then all ages outside 18–150 are treated as invalid and replaced with a missing value. Missing dates also produce a missing age. using code: 

df.loc[
    ~df["customer_age_years"].between(18, 150),
    "customer_age_years"
] = pd.NA

Missing ages are replaced with the average of the valid ages.

Corrections to delivery_days calculation include adjusting the delivery dates by adding 7860 days to results that give negative delivery_dates. This hand coded correction ensures the delivery dates resulting in negative results are recalculated
using code: 

print(f"Negative delivery durations to adjust: {negative_mask.sum()}")
df.loc[negative_mask, "delivery_date"] += pd.Timedelta(days=7860)

Added new features- delivery_method, delivery_status and Insurance _status to find out if there is any relationship between returns and the method of delivery (Road, Shipping, Flight), the status in which the goods arrive after delivery (Minor damage, slight damage, no damage) and insurance provision on goods.

The code assigns a method based on delivery time:

Fewer than 7 days = "Flight"
7–13 days = "Road"
14 or more days = "Shipping"

If delivery_days is missing, no condition matches, so the method remains missing.

code used: df["Delivery_method"] = pd.NA
df.loc[df["delivery_days"] < 7, "Delivery_method"] = "Flight"
df.loc[df["delivery_days"].between(7, 13), "Delivery_method"] = "Road"
df.loc[df["delivery_days"] >= 14, "Delivery_method"] = "Shipping"

Each delivery method is mapped to a status. Missing or unmapped methods produce a missing status using code: 
status_by_method = {
    "Road": "slight damage",
    "Flight": "no damage",
    "Shipping": "minor damage",}
df["Delivery_status"] = df["Delivery_method"].map(status_by_method)

Everyone starts as "not insured". A row becomes "insured" only if the item costs more than 50 and the delivery method is Flight or Shipping. code used:

df["Insurance_status"] = "not insured"
insured_condition = (
    (df["item_price"] > 50)
    & df["Delivery_method"].isin(["Flight", "Shipping"]))
df.loc[insured_condition, "Insurance_status"] = "insured"

Python row 21:

This code creates a separate DataFrame containing only those columns to help prevent unintended changes to the original df
model_columns = [
    "customer_age_years",
    "Delivery_method",       
    "Delivery_status",      
    "Insurance_status",
    "order_item_id",
    "item_id",
    "item_size",
    "item_color",
    "brand_id",
    "item_price",
    "user_state",
    "return"]

model_df = df[model_columns].copy()

model_df = model_df.replace([np.inf, -np.inf], np.nan)
model_df = model_df.dropna(subset=["return"]).copy()
Infinite values are changed to missing values. Rows with a missing "return" are then removed because they have no known answer for training or evaluation at this point.

          
X = model_df.drop(columns=["return"]) X contains the input features.
y = model_df["return"].astype(int) y contains the target values the model will learn to predict.
      
.astype(int) is just converts the target to integers, as expected for many classification tasks. This assumes "return" contains values that can be converted to integers, such as 0 and 1.


Identify numeric and categorical columns

numeric_features = [...]
categorical_features = [...]

The code treats some columns as numbers and others as categories.
This matters because the two types need different preprocessing required numeric data to be scaled, while categories such as "Flight" or "blue" need to be encoded. I included a build preprocessing pipelines

Numeric pipeline

numeric_pipeline = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())])
      For numeric columns:[
    "customer_age_years",
    "order_item_id",
    "item_id",
    "brand_id",
    "item_price"]

Missing values are filled with that column’s median. Values are standardized so they are centered around zero and have roughly comparable scales.

Categorical pipeline

categorical_pipeline = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(
        handle_unknown="ignore",
        sparse_output=False))])
      For categorical columns:[
    "Delivery_method",
    "Delivery_status",
    "Insurance_status",
    "item_size",
    "item_color",
    "user_state"]

Missing values are filled with the most common category.


handle_unknown= "ignore" (prevents errors if the test data contains a category that was not present in the training data) sparse_output= "False" (asks for a regular dense array rather than a sparse matrix)

I then combined the pipelines using code:

preprocessor = ColumnTransformer 
(transformers=[("num", numeric_pipeline, numeric_features),
               ("cat", categorical_pipeline, categorical_features)])

Because one cannot process numbers and text the same way. This setup allows me to clean, scale and encode the dataset in one clean before production pipelines to prevent any data leakages.

This code is the set of instructions for doing that:

("num", numeric_pipeline, numeric_features)
means: Use numeric_pipeline on the number columns.

("cat", categorical_pipeline, categorical_features)
means: “Use categorical_pipeline on the word columns.

So ColumnTransformer is the organizer: it sends each column to the right set of instructions, then joins the prepared columns back together.

ColumnTransformer () function helps split the dataset manually, so that you target specific columns for cleaning and transformation then combined them automatically later.


Split the data before fitting preprocessing.

Data is split into training and testing sets before preprocessing to prevent data leakage.
Data leakage happens when information from your test set accidentally leaks into your training process. The split happens before fitting the imputer, scaler, and encoder to avoid data leakage. If preprocessing were fitted using the test set, information from that set could influence the training process.

This code is the set of instructions for doing that:

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.20,
    random_state=42,
    stratify=y)
          
This reserves 20% of the rows for testing and uses the remaining 80% for training.

random_state=42 makes the split reproducible.

stratify=y tries to preserve the target-class proportions in both sets. 

Fit preprocessing on training data, then apply it to both sets

X_train_encoded = preprocessor.fit_transform(X_train)
X_test_encoded = preprocessor.transform(X_test)
      
fit_transform learns preprocessing details from the training data using statistical methods such as medians, common categories and scaling statistics—and transforms the training features.
transform applies those same learned details to the test features. It does not relearn them from the test data.

feature_names = preprocessor.get_feature_names_out() function retrieves names for the processed features after learning the preparation rules from the training data, uses those rules on the test data and get the names of the prepared columns.

Convert the processed arrays back to DataFrames

X_train_final = pd.DataFrame()
X_test_final = pd.DataFrame()

Scikit-learn preprocessing returns arrays. These lines turn the arrays into pandas DataFrames with feature names, making the results easier to inspect.



















































.
