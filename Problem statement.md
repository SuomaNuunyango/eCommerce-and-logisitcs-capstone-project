# eCommerce-and-logisitcs-capstone-project

This project studies an online South African retail store called Stadioalot. 

**Problem Statement**

Stadioalot’s apparel and shoe (product) return rate increased from 22% in 2025 to 29% in 2026,while its overall return rate increase from 11% (2025) to 15% in 2026, reducing retail profit margins and increasing storage, handling, and logistics costs. The company currently processes returns reactively and has no systematic way to identify high-risk products or orders before shipment. This limits its ability to take proactive preventive action, plan inventory, or provide customers with more consistent product and delivery experiences.

The issue affects Stadioalot’s profitability, customers satisfaction and the workload of warehouse and logistics teams. Although the company holds three to five years of relevant historical data which includes returns and return reasons, customer reviews, product quality and damage reports, delivery records, inventory, warehouse costs and return policies have not been integrated into their existing data sources to develop the analytical capability to turn them into actionable return-risk predictions. There is a data and decision-making gap rather than a failure of its existing pick, pack, and ship operations.
The project will use these historical data to develop and evaluate a predictive system that identifies products or orders at elevated risk of return before shipment. The company's business target is to reduce avoidable returns by 30–40% within 18 months, with the stated goal of lowering the overall return rate to 10%. Predictions should support practical interventions such as investigating product quality or descriptions, improving delivery performance, adjusting purchasing and promotions and planning inventory and warehouse capacity rather than relying on blanket removal of products or customers. This will prevent the company from making rash decisions, such as removing high-yield products from its portfolio without data-driven evidence.

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

---

Target:
Reduce avoidable returns by 30-40% over 18 months, targeting a return rate of 15-10% (below industry average of 20-25%).

Stadioalot has not yet connected its data to predict and prevent returns at scale. This means the company has the potential to improve its financial burden and reduce overall return rates even to 0%. by cutting out sales of high return risk products, improving delivery time, reducing warehousing costs and taking proactive actions that align with their strategic goals that ultimately improve company profits, add value to the customer experience with retail products.

---
# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


