# eCommerce-and-logisitcs-capstone-project

This project studies an online South African retail store called Stadioalot. 

Current Situation:
Stadioalot generates R38M annually, with 54% from retail sales and 27% from its marketing platform. The company's machine-driven pick, pack, and ship operations are highly efficient. However, product returns have increased from 22% (2025) to 29% (2026), eroding retail profit margins and increasing warehouse costs. The company has no systematic method to identify which products are likely to be returned before they are shipped.

Core Problem:
Stadioalot cannot predict which products will be returned, meaning it cannot:

1. Flag high-risk products before shipping

2. Warn customers about products with high return rates

3. Adjust pricing or marketing for high-return products

4. Allocate warehouse space efficiently

Decision to Improve:
Which products should be flagged as high-return-risk, and what action should be taken (additional quality check, customer warning or removal from marketing to focus on core sales stream)?

Current Baseline:
No systematic return risk flagging system exists. Returns are processed reactively. The current return rate is 29% up as of 2026. Stadioalot doesn't have an operational failure but a data failure. It has 3-5 years of historical data on customer reviews, delivery records, customer service contracts, product catalogues, order transactions, inventory and warehouse  but lacks analytical capabiliies and technologies to gain predicitve insight to study behavioural and hidden patterns from the data.

Proposed Data Science Approach:

1. Classification model (logistic regression, random forest, XGBoost) to predict return likelihood

2. NLP on customer reviews to extract sentiment and complaint themes

3. Feature engineering from delivery time, product category, customer history, quality scores

4. Evaluation using precision, recall, F1 (accounting for 29% class imbalance)

5. Baseline comparison against current no-flagging approach

## Data Assets for Stadioalot Return Prediction

| Data Asset | Variables Needed | Findings |
|------------|------------------|----------|
| Historical returns | Product ID, return reason, date, customer ID | Target variable |
| Customer reviews | Star ratings, text, date, expressions (emojis) | Sentiment predicts returns |
| Quality scores | Internal rating, defect rate | Quality drives returns |
| Delivery data | Expected delivery vs actual date, location | Late delivery's correlation with returns |
| Inventory sheets | Stock levels, warehouse location, product expiration date | Overstocking indicates high-return products |
| Warehouse costs | Storage cost per product, warehouse location | Holding cost per returned product |
| Return policies | Policy text, return window | Policy changes affect returns |
| Damage reports | Product ID, defect type | Direct predictor |


Target:
Reduce avoidable returns by 30-40% over 18 months, targeting a return rate of 15-18% (below industry average of 20-25%).

Stadioalot has not yet connected its data to predict and prevent returns at scale. This means the company has the potential to improve its financial burden and reduce overall return rates even to 0%. by cutting out sales of high return risk products, improving delivery time, reducing warehousing costs and taking proactive actions that align with their strategic goals that ultimately improve company profits, add value to the customer experience with retail products.

---

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


