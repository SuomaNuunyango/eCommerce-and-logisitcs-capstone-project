#Preprocessing details to the BADS_WS1920_known.csv (Training dataset).

The following details are subject to change based on improvements to the python code

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

Categorical data cleaning was performed iteratively across the four primary features: item_size, item_color, user_title, and user_state. Each column underwent a standardized preprocessing pipeline: .astype("string") enforced consistent data types, .str.strip() eliminated leading and trailing whitespace, and .str.lower() normalized the text to prevent duplicate categories caused by casing variations.Following standardization, item_color was identified as the only column containing missing values. Because the missing data accounted for a negligible 0.06% of total records, mode imputation via .mode(dropna=True) was applied to fill the blanks with the most frequent color. This approach successfully handled the missing data without compromising the integrity of the dataset.




















