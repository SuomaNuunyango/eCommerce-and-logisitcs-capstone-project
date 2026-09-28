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
