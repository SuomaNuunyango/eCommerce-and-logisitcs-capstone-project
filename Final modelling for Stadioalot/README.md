This  folder contains the client's Random forest model for predicting online product returns based on historical data given by Stadioalot.

The final model file is available as [SS3_PartB.ipynb](https://github.com/SuomaNuunyango/eCommerce-and-logisitcs-capstone-project/blob/main/Final%20modelling%20for%20Stadioalot/SS3_PartB.ipynb).

Libraries to be imported for the code before running it are: 

`joblib=1.6.0`

`matplotlib=3.10.8`

`numpy=2.5.4`

`pandas=3.0.1`

`scikit-learn=1.9.1`

`seaborn=0.13.2`

Python row 1

This code is designed to load five CSV files into Python using pandas and perform an initial data quality check on each file. 

There are two imports here:

from pathlib import Path

`pathlib` is a Python library for working with file and folder paths.

`Path` helps you construct paths in a way that works across different operating systems.

The "." means the current working directory (the folder Python is currently working in).

`DATA_DIR` that represents the folder where the CSV files are expected to be located.

The list of raw data is contained in FILES = {
    "returns": "table1_sales_returns.csv",
    "reviews": "table2_customer_reviews.csv",
    "deliveries": "table3_delivery_data.csv",
    "inventory": "table4_inventory.csv",
    "policies": "table5_return_policies.csv",}

    















