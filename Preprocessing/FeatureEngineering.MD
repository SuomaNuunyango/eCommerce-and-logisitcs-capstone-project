**Preprocessing details to the BADS_WS1920_known.csv (Training dataset).**

The following details are subject to change based on improvements made to the python code called [Feature engineering.ipynb](Preprocessing/Feature engineering.ipynb) file .

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
