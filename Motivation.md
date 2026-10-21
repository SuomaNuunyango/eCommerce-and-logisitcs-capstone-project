# eCommerce-and-logisitcs-capstone-project

This project studies an online South African retail store called Stadioalot. 

**Current Situation:**
Stadioalot generates R38M annually, with 54% from retail sales and 27% from its marketing platform. The company's machine-driven pick, pack, and ship operations are highly efficient. However, product returns have increased from 22% (2025) to 29% (2026), eroding retail profit margins and increasing warehouse costs. The company has no systematic method to identify which products are likely to be returned before they are shipped.

**Core Problem:**
Stadioalot cannot predict which products will be returned, meaning its current system cannot:

1. Flag high-risk products before shipping them to customers

2. Warn sales department about products with high return rates risks to reduce reorder

3. Adjust pricing or marketing for high-return products

4. Allocate warehouse space efficiently on expected product returns

5. Control inventory levels and prevent obsolescence from expected product returns
   

**Stakeholders affected:**

Stadioalot firm: loss of profit margins and incurs higher warehouse costs

Customers: experience inconsistent product satisfaction and delivery outcomes

Warehouse and logistics teams: face increasing strain from processing product returns


**Current Baseline:**
No systematic return risk flagging system exists. Returns are processed reactively. The current return rate is 29% up as of 2026. Stadioalot doesn't have an operational failure but a data failure. It has 3-5 years of historical data on customer reviews, delivery records, customer service contracts, product catalogues, order transactions, inventory and warehouse  but lacks analytical capabiliies and technologies to gain predicitve insight to study behavioural and hidden patterns from the data.

Stadioalot’s return rate has risen from 22% in 2025 to 29% in 2026 a 7 percentage point increase that threatens retail profit margins and adds warehouse and logistics costs. Because returns are handled reactively and the company has no system to identify high-risk orders before shipment, so it misses opportunities to prevent avoidable returns, improve customer satisfaction, and plan inventory and warehouse capacity. Addressing the problem is important to protect profitability, reduce operational strain, and make better use of the company’s existing data.

Stadioalot should develop a data-driven return-risk system using its historical transaction, product, delivery, inventory, customer-service, and review data. Classification models such as logistic regression, Random Forest and XGBoost could estimate the likelihood of a return for each order item. Review text could also be analysed with natural language processing to identify recurring complaints and product-quality concerns, while features such as delivery time, product category and customer history could help reveal return patterns. The model should be evaluated against the current no-flagging approach using precision, recall, and F1 score, with particular attention to identifying likely returns without creating too many false alarms. High-risk predictions could then guide targeted actions like, checking product descriptions or quality, alerting sales teams, adjusting promotions or reordering and improving inventory and warehouse planning. The system should be piloted and monitored over time to confirm that it reduces returns and costs without harming the customer experience.

Proposed Data Science approach:

1. Classification model (logistic regression, random forest, XGBoost) to predict return likelihood.

2. NLP (Natural language processing) on customer reviews to extract sentiment and complaint texts themes

3. Feature engineering from delivery time, product category, customer history, quality scores into predictive signals that expose hidden patterns for machine learning models.

4. Evaluation using precision, recall, F1 (accounting for 29% class imbalance) to score model performance.

5. Baseline comparison of current no-flagging approach against predictive model flagging of product return.

---
# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


