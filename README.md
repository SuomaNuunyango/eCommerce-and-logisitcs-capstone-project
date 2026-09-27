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

Proposed Data Science approach:

1. Classification model (logistic regression, random forest, XGBoost) to predict return likelihood.

2. NLP (Natural language processing) on customer reviews to extract sentiment and complaint texts themes

3. Feature engineering from delivery time, product category, customer history, quality scores into predictive signals that expose hidden patterns for machine learning models.

4. Evaluation using precision, recall, F1 (accounting for 29% class imbalance) to score model performance.

5. Baseline comparison of current no-flagging approach against predictive model flagging of product return.

## Data assets to be used for Stadioalot return prediction (3-5 years historical data)

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
## Project RAAIDD Log 

| RAAIDD | Description |
|--------|-------------|
| **Risks** | 1. **Data quality and availability issues:** Since the data to be analysed dates back 3-5 years. Historical sales return data from 2022–2023 might contain incomplete fields and missing variavles causing the model to perform predictions on outdated products/ once of products that where trending then. <br>2. **Incomplete data entry:** Stadioalot online retail staff might opt to select default options like "other" or "damaged" to speed up the process causing the analysis performed by the model to create bias analysis on dominating products. This lcan result in anaylysing data with vague or missing information about why the product actually came back. <br>3. **Model performance risk:** The classification model may achieve high overall accuracy (e.g., 85%) but low recall for the minority "returned" class (29%), causing Stadioalot to miss high-risk products. <br>4. **Lacking of qualitative context:** Data can only show what happened, but not always why. A spike in returns might be due to a confusing sizing chart online, organised retail fraud (customers using item once and returnung it) rather than a manufacturing defect in the product itself. <br>5. **Regulatory risk:** Customer review text and delivery location data may contain customer personal information, and processing it for sentiment analysis without POPIA compliant can violate thr customers right to privacy potentially exposing Stadioalot to non compliance fines.|
| **Actions** | 1. **Data request (Phase 1):** Searching for atleast 3 datasets similar to Stadioalot's databases containing (historical returns, customer reviews, quality scores, delivery data, inventory sheets, warehouse costs, return policies, damage reports). <br>2. **Data preprocessing (Phase 2):** Data cleaning and preprocessing for selected dataset for missing values, duplicates, encoding categorical variables using (Scikit-learn on Python), extracting sentiments from customer reviews using NLP, and inconsistent formats; document all data quality issues for the client. <br>3. **Model training and fitting (Phase 3):** Split data into training (70%), validation (15%), and test (15%) sets, ensuring stratified sampling to preserve the 29% return rate. <br>4. **Model performance evaluation (Phase 4):** Train and evaluate three classification models (logistic regression, random forest, XGBoost), compare the models performance using precision, recall and F1 against the non flagging baseline to examing models overall performance. <br>6. **Visualisation preparation and Model reporting (Phase 5):** In this final stage, I will interpret the model results for StadioAlot’s management, generate SHAP feature importance plots, and compile a comprehensive model fact sheet. The final deliverables will include a formal report and a 15-minute executive presentation detailing overall model performance and its strategic value in predicting and mitigating high risk returns.|
| **Assumptions** | 1. **Data availability:** We assume Stadioalot's datasets are easily available and accessible for use within reasonable time on demand for project tracking as per project lifecycle plan. <br>2. **Data integrity:** We assume that Product ID and customer ID are automatically generated by the system and consists of atleast the same format across all records, allowing reliable joins without manual mapping. <br>3. **Business adoption to data driven approach:** We assume Stadioalot's management will act on the model's output by flagging high-return-risk products before shipping, rather than using the score only for post-hoc reporting. <br>4. **Regulatory compliance:** We assume Stadioalot has obtained the necessary POPIA consent from customers to use their review text and location data for project analysis and insights aimed at improving the customer experience. This intended use was also communicated to customers prior to data collection. <br>5. **Model generalisation:** We assume the 29% return rate is stable enough that a model trained on historical data will generalise to future returns, with no major product-mix shift during the project. <br>6. **Model's legal protection:** We assume Stadioalot has initiated all appropriate clause and copyright for the model to protect the original creative expressions, documentation, or source code used to create or implement the model. |
| **Issues** | **Main issue:** The delay in obtaining a complete dataset that is free from structural discrepancies and major variable omissions ultimately increased the time required for data preprocessing and cleaning. |
| **Decisions** | **Main decision:** The cleaning techniques are flexible, ensuring the data maintains its originality and integrity. If an approach is too aggressive and alters the original text or structure significantly, we can pivot to alternative techniques that preserve data quality without compromise. |
| **Dependencies** | 1. **Pandas Profiling and OpenRefine:** Using Pandas profiling to inspect the datasets for missing values, duplicates, inconsistent formats, and outliers. Using OpenRefine to clean and preprocess the data. <br>2. **Git and DVC:** Git tracks every version of the Python notebook that cleans the slaes returns data and records the exact commit where the train/test split was made, so results are reproducible, while DVC (Data Version Control) Tracks versions of the actual data files and stores data snapshots at each cleaning stage. <br>3. **Great Expectations and Pydantic:** Great Expectations and Pydantic are tools that act like strict proofreaders. They check the data against a set of rules (e.g., "no blank IDs allowed," "dates must be real dates"). <br>4. **Asana Gantt charts:** this tool shows who's doing what, and when, on a timeline and what might have been skipped. It highlights critical paths of the project lifecycle and causes of delay to the next phase by showing Stadioalot's management acionable plans and progress <br>5. **Statisical Modelling:** Using Scikit-Learn to predict items that are likely to be returned and K-Means clustering to segment cusotmers that are highly to become serial retruners of items. |

---
# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


