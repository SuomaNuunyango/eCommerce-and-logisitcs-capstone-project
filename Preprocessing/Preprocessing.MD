#Preprocessing details to the BADS_WS1920_known.csv (Training dataset).

The following details are subject to change based on improvements made to the python code.

Python row 46: 


imported the relevent libraries needed for preprocessing. 

**import pandas as pd
from pathlib import Path** 


Panda turns the raw text data into DataFrame which makes it easy to  clean.
Pathlibhelps find the csv.file on the computer and turns text strings into smart path objects.

Python row 32:

Inspecting the dataset of the predetermined columns needed to before training the models selected. required_columns = [
    "order_item_id",
    "order_date",
    "delivery_date",
    "item_id",
    "item_size",
    "item_color",
    "brand_id",
    "item_price",
    "user_id",
    "user_title",
    "user_dob",
    "user_state",
    "user_reg_date",
    "return"]
If the list isn't empty the code will display an error naming the missing column using this code: 
**if missing_columns:
    raise ValueError(
        f"The following required columns are missing: {missing_columns}")**


Python row 24-25:

This step inspects the dataset for duplicate rows and columns using the duplicated() function. If duplicates are found, they are removed using the drop_duplicates() and transposition methods. Eliminating duplicate rows and columns is critical to preventing bias and false patterns, which can skew our analytics and cause the machine learning model to overfit during training.


Python row 30-31, 42 and 47:

This cell converts all date columns into pandas datetime objects. Standardizing the date format is essential because these columns serve as independent variables for calculating derivative metrics, such as user age or delivery delays (the time elapsed between the order date and delivery date). Setting errors='coerce' automatically transforms invalid dates into NaT (Not a Time) missing values, allowing us to easily identify and handle unparseable data.

date columns inspected= [
    "order_date",
    "delivery_date",
    "user_dob",
    "user_reg_date"]

Date scaffolding was implemented to handle unparseable values within the delivery_dates and user_dob columns. To preserve data integrity and retain 9,318 delivery records and 8,725 user date-of-birth records otherwise flagged as missing (NaT), these variables were mapped onto continuous date ranges. Utilizing a continuous timeline allows the model to handle these records constructively without resorting to data deletion.


Python row 36:

Categorical data cleaning was performed iteratively across the four primary features: item_size, item_color, user_title, and user_state. Each column underwent a standardised preprocessing pipeline: .astype("string") enforced consistent data types, .str.strip() eliminated leading and trailing whitespace, and .str.lower() normalised the text to prevent duplicate categories caused by casing variations.Following standardisation, item_color was identified as the only column containing missing values. Because the missing data accounted for a negligible 0.06% of total records, mode imputation via .mode(dropna=True) was applied to fill the blanks with the most frequent color. This approach successfully handled the missing data without compromising the integrity of the dataset.


Python row 38:

Converting the listed columns to numeric columns data type. numeric_columns = [
    "order_item_id",
    "item_id",
    "brand_id",
    "item_price",
    "user_id"]
pd.to_numeric() function converts the columns values to numbers. 
errors="coerce" function turns values that cannot be converted to Nan (missing values) to identify how many columns are containing non convertible so that they can be engineered to a preferred standard/ format. NaN values are imputed with the mean accept, user_id column which was first converted to "anonymous" to calculate if the total count is below 10%. I applied a rule that should the count percentage is below 10% then the column anonymous will be replace with the mean ID, otherwise drop the column. 10% is reasonable as it would insignificantly reduce the quality of the data if the user_id is imputed with the mean.


Python row 42

The return_target column values are classified into binary outcome lables of 1 & 0 using code df["return"] = pd.to_numeric(df["return"], errors="coerce"), where errors=("coerce") finds the blanks and invalid answers to report an error. 
All missing and invalid values exisitng will stop the code from reading and report an error by using code if missing_count > 0:
    raise ValueError("The target column 'return' contains missing values.").

To confirm that the convertion of values was successful to 0 and ! only, I used if not unique_target_values.issubset({0, 1}):
    raise ValueError("The 'return' column must contain only 0 and 1.")
To print the totals upon successful conversion a print outcomes return counts of 1 with percentage and for not returned it counts the 0 with percentage.









