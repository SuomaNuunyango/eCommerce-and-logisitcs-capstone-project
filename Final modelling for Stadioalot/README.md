This  folder contains the client's Random forest model for predicting online product returns based on historical data given by Stadioalot. Predictions are based on pre delivery to flag returns before client even gets the product.

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

 I then created a empty dataframe to store successfully loaded files. dataframes = {
    "returns": returns_dataframe,
    "reviews": reviews_dataframe,
    "deliveries": deliveries_dataframe,
    "inventory": inventory_dataframe,
    "policies": policies_dataframe} 

Dataset was inspected for missing values in each file. Then print displays the information about the dataset including counts and percentages of missing values.

Python row 2

The code cleans and standardises the delivery dataset by correcting column names, formatting courier partner names consistently, converting delivery dates into a suitable format, and removing records with missing required information. It then calculates the absolute difference between expected and actual delivery dates in days. 

Finally, it groups the data by courier partner and calculates the mean delivery time difference, the most common difference, and the number of records for each courier. 

The purpose is to make the delivery data consistent and summarise delivery-date differences across courier partners, allowing for easier comparison of delivery performance.

Python row 13

After loading the five CSV datasets, I standardised the column names filled the missing value using imputation procedures. 

For sales returns, it replaces missing or blank refund methods with “Other”; for delivery data, it standardises courier names, converts delivery dates, and estimates missing actual delivery dates using each courier’s average delay; 

for inventory, it removes rows with missing expiration dates

for customer reviews, it fills missing review text using the most frequent existing review text for the corresponding star rating. 

It saves the processed datasets as new preprocessed CSV files and reports any remaining missing values by displaying each dataset’s dimensions and missing-value statistics. The code also checks for required columns and handles missing files or processing errors. Its overall purpose is to improve data consistency and completeness while preserving the original files, although some imputation methods may introduce assumptions that should be evaluated before further analysis.

Python row 4

The code performs a final preprocessing step on the five datasets by standardising text formatting, preserving IDs as strings, converting date columns to datetime format, assigning appropriate numeric data types and normalising Boolean values into True and False. 

It preserves the original content of free-text fields, such as customer reviews and return policies, while standardising other text labels to lowercase. 

It then saves each processed dataset as a new CSV file named `preprocessed_returns.csv`, `preprocessed_reviews.csv`, `preprocessed_deliveries.csv`, `preprocessed_inventory.csv`, and `preprocessed_policies.csv`. 

Finally, it reports the row counts, output file locations, data types and any missing or unparseable dates. The purpose is to ensure that the datasets have consistent formats and appropriate data types, making them more reliable and ready for further analysis.

Python row 5

The code checks the quality of date values in the preprocessed customer reviews and delivery datasets. It removes any leading or trailing whitespace from column names, and verifies that the specified date column exists. It then convert the values in that column into datetime format, counting any missing or unparseable dates. 

Finally, it calculates and prints the number and percentage of unparseable dates in each dataset. 

If a specified column is not found, it displays the available column names and moves on to the next file. The purpose is to validate date formatting and identify potential data-quality issues before further analysis. Note that the check counts existing missing values as well as invalid date values, so it does not distinguish between the two.

Python row 6

The code handles missing or invalid dates for deliveries, it converts the dispatch and expected delivery dates to datetime format, fills missing dispatch dates by subtracting three days from the expected delivery date, and saves the updated dataset. 

It then reports how many review rows were removed and how many dispatch dates remain missing. The purpose is to improve date completeness and consistency so the datasets are more suitable for further analysis.

Python row 7

The code verifies whether date parsing was successful in the preprocessed customer reviews and delivery datasets. It loads each CSV file, removes whitespace from column names, and checks whether the specified date column exists. 

It then attempts to convert the date values into datetime format and counts any values that are missing or cannot be parsed. 

Finally, it reports the number and percentage of unparsed dates for each file, or lists the available columns if the expected column is not found. The purpose is to confirm the effectiveness of the earlier date cleaning steps and identify any remaining date quality issues.

Python row 8

The code identifies and removes duplicate records from the preprocessed delivery dataset. It loads the CSV file, counts the duplicate rows while keeping the first occurrence, and removes the additional duplicates.

Python row 9

The code links the delivery and sales returns datasets using the shared `order_id` column. 

It first checks that both files contain this column, then standardises the order IDs by converting them to strings and removing extra whitespace to reduce matching errors. It identifies all order IDs appearing in the returns dataset and creates a new column called `return_flag`, which I set as target feature. 

In the delivery dataset: 1 indicates that an order was returned, while 0 indicates that it was not returned. 

The updated delivery dataset is saved to the original file, and the code prints the counts of returned and non-returned orders. The purpose is to identify returned orders within the delivery data, enabling further analysis of return patterns and delivery performance.


Python row 10

The code builds and tunes a machine learning model (Random Forest) to predict whether a delivered order will be returned.  

It loads and validates the delivery dataset, filters for orders delivered between January and June 2026 and creates features such as `courier partner`, `delivery region`, `transit time`, `lateness` and `dispatch date and time`. 

It uses a chronological split to separate the data into training (January–April), validation (May) and test (June) sets,  

(Why?) this simulates predictions on future orders. A preprocessing pipeline handles missing numeric and categorical values and converts categorical variables into a format suitable for machine learning. 

A Random Forest classifier is then tuned using grid search and three-fold stratified cross-validation on the training data, with ROC-AUC as the selection metric. 

Finally, the code displays the best cross-validation ROC-AUC score and selected hyperparameters. The purpose is to develop a model that identifies factors associated with returns and assesses its potential predictive performance. 

Python row 11

The code selects an appropriate decision threshold for the trained Random Forest model by testing multiple thresholds against the validation dataset. It prioritises achieving a minimum recall of 40% for returned orders, then selects the threshold with the highest validation accuracy among those meeting this requirement, favouring fewer false positives in the event of a tie. 

It reports the selected threshold and its validation performance, displays a comparison table, and generates plots showing how changes in the threshold affect accuracy, precision, recall, false positives, and false negatives. 

It then defines an evaluation function to assess the model on the training, validation, and unseen test datasets using metrics such as `accuracy`, `precision`, `recall`, `F1-score`, `ROC-AUC` and a `confusion matrix`. 

Finally, it combines the results into a comparison table. The purpose is to balance the model’s ability to identify returned orders against the risk of incorrectly flagging orders and to evaluate how well it performs on unseen data.

Python row 14

The code visualises and summarises the Random Forest model’s performance by comparing accuracy, precision, recall, F1-score, and ROC-AUC across the training, validation, and unseen test datasets.

It generates a confusion matrix and an ROC curve for the June test set to show how effectively the model identifies returned orders and distinguishes between the two classes. 

It also extracts and plots the 15 most important features used by the model to make predictions. 

Finally, it saves the trained model `pipeline`, `feature list`, `target variable`, and `prediction timing` information into a [`.joblib`](https://github.com/SuomaNuunyango/eCommerce-and-logisitcs-capstone-project/blob/main/Final%20modelling%20for%20Stadioalot/return_flag_random_forest.joblib) file so the model can be reused later without retraining. The purpose is to communicate the model’s predictive performance, understand which features contribute most to its decisions, and preserve the trained model for future use.








