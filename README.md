# eCommerce-and-logisitcs-capstone-project

This project studies an online South African retail store called Stadioalot. 

Current Situation:
Stadioalot generates R38M annually, with 54% from retail sales and 27% from its marketing platform. The company's machine-driven pick, pack, and ship operations are highly efficient. However, product returns have increased from 22% (2025) to 29% (2026), eroding retail profit margins and increasing warehouse costs. The company has no systematic method to identify which products are likely to be returned before they are shipped.

Core Problem:
1. Stadioalot cannot predict which products will be returned, meaning it cannot:

2. Flag high-risk products before shipping

3. Warn customers about products with high return rates

4. Adjust pricing or marketing for high-return products

5. Allocate warehouse space efficiently

Decision to Improve:
Which products should be flagged as high-return-risk, and what action should be taken (additional quality check, customer warning, or removal from marketing)?

Current Baseline:
No systematic return-risk flagging exists. Returns are processed reactively. The current return rate is 29% and rising.

Proposed Data Science Approach:

1. Classification model (logistic regression, random forest, XGBoost) to predict return likelihood

2. NLP on customer reviews to extract sentiment and complaint themes

3. Feature engineering from delivery time, product category, customer history, quality scores

4. Evaluation using precision, recall, F1 (accounting for 29% class imbalance)

5. Baseline comparison against current no-flagging approach

Target:
Reduce avoidable returns by 30-40% over 18 months, targeting a return rate of 15-18% (below industry average of 20-25%).

Stadioalot has not yet connected its data to predict and prevent returns at scale. This means the company has the potential to improve its financial burden and reduce overall return rates even to 0%. by cutting out sales of high return risk products, improving delivery time, reducing warehousing costs and taking proactive actions that align with their strategic goals that ultimately improve company profits, add value to the customer experience with retail products.

improving delivery time, reducing warehousing costs and taking proactive actions that align with their strategic goals that ultimately improve company profits, add value to the customer experience with retail products.
