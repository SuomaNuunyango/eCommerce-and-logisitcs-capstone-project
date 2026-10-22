# STADIOalot — eCommerce & Logistics Returns: Data Extract

Six months of operational data (1 January to 30 June 2026) covering **14,000 dispatched orders across 610 products and four warehouses**. Identifiers follow the formats set out in the data request: `RET-YYYY-NNNNN`, `ORD-YYYY-NNNNN`, `DEL-YYYY-NNNNN`, `INV-YYYY-NNNNN`, `REV-YYYY-NNNNN`, `POL-YYYY-NNN`, `CUST-NNNNN`, and category-coded product IDs such as `FASH-DRSS-412`. Datetimes are `yyyy-MM-dd HH:mm:ss`. All amounts are ZAR including VAT.

## Files

### `table1_sales_returns.csv`
Items returned from online purchases. One row per return.  
Rows: 2,759

| Column | Description |
|---|---|
| `Return ID` | String |
| `Order ID` | String |
| `Product ID` | String |
| `Customer ID` | String |
| `Return date and time` | Datetime |
| `Return reason` | Categorical |
| `Returned quantity` | Integer |
| `Return item value` | Numeric |
| `Return status` | Categorical |
| `Refund method` | Categorical |

### `table2_customer_reviews.csv`
Customer ratings and free-text feedback on products. One row per review.  
Rows: 3,881

| Column | Description |
|---|---|
| `Review ID` | String |
| `Product ID` | String |
| `Customer ID` | String |
| `Review date &time` | Datetime |
| `Star rating` | Integer |
| `Review text` | String |
| `Verified buyer` | Boolean |

### `table3_delivery_data.csv`
Transit records for dispatched orders. One row per delivery.  
Rows: 14,042

| Column | Description |
|---|---|
| `Delivery ID` | String |
| `Order ID` | String |
| `Dispatch date & time` | Datetime |
| `Expected delivery date` | Datetime |
| `Actual delivery date` | Datetime |
| `Delivery location` | String |
| `Delivery status` | Categorical |
| `Courier Partner` | Categorical |

### `table4_inventory.csv`
Current stock position per product per warehouse, with storage and return-handling costs.  
Rows: 1,389

| Column | Description |
|---|---|
| `Inventory record ID` | String |
| `Product ID` | String |
| `Stock on hand` | Integer |
| `Warehouse location` | Categorical |
| `Reorder point` | Integer |
| `Expiration date` | Datetime |
| `Courier Partner` | Categorical |
| `Storage cost per unit` | Numeric |
| `Handling cost per return` | Numeric |

### `table5_return_policies.csv`
Return rules by product category, including the return window.  
Rows: 8

| Column | Description |
|---|---|
| `Policy ID` | String |
| `Product category` | Categorical |
| `Return window (days)` | Integer |
| `Policy text` | String |
| `Effective date & time` | Datetime |
| `Electonic signature` | Boolean |

## Joining the tables

| From | To | Key |
|---|---|---|
| `table1_sales_returns` | `table3_delivery_data` | `Order ID` (every returned order has a delivery record) |
| `table1_sales_returns` | `table4_inventory` | `Product ID` |
| `table1_sales_returns` | `table2_customer_reviews` | `Customer ID` + `Product ID` |
| `table2_customer_reviews` | `table4_inventory` | `Product ID` |
| `table1_sales_returns` | `table5_return_policies` | product category, from the `Product ID` prefix |

The `Product ID` prefix carries the category: `ELEC` Electronics, `FASH` Fashion, `NIK` Sports,
`HOME` Home & Garden, `BTY` Beauty, `TOY` Toys, `BOOK` Books. Use it to join to the policy table,
which keys on `Product category`.

About 96% of `Product ID`s in returns and reviews appear in the inventory table; the remainder are
lines no longer stocked in any warehouse.

## An important gap in the request

The request asks for returns, reviews, deliveries, inventory and policies — but **not for a sales
or orders table**, even though `Order ID` is described as linking to "the sales transaction table".
That table is therefore not in this extract.

The consequence matters for modelling: `table1_sales_returns` contains **only orders that were
returned**. There are no non-returned orders in it, so it cannot by itself support a model that
predicts whether an order will be returned — there are no negative cases.

`table3_delivery_data` is the usable substitute. It holds all 14,000 dispatched orders, returned or
not, so a return flag can be derived as "this `Order ID` appears in table 1". Build the modelling
population from the delivery table and join the returns on, rather than the other way round. If a
proper orders table becomes available, request it.

## What is in the data

- **Overall return rate** is about 22% of delivered orders, but it varies sharply by category: Fashion and Sports are the highest, Books and Beauty the lowest.
- **Late delivery lifts returns** — orders that arrived after the promised date are returned 28.4% of the time against 20.8% for on-time orders.
- **Couriers differ materially** on punctuality: DHL Express is late on 8% of deliveries, FedX 13%, Internal Fleet 23%, third-party logistics 30%. Overall 17.3% of delivered orders arrive late.
- **Return reasons track the category** — Fashion returns are 43% size/fit issues, while Electronics, Home & Garden and Toys are dominated by damage and "not as described".
- **Reviews carry signal**: orders that were returned average 2.25 stars against 3.93 for orders that were not.

## Points to resolve before modelling

- `Return reason`, `Return status` and `Refund method` are recorded **after** a return has happened. None may be used as a predictor of whether a return will occur — they are outcomes, not inputs.
- `Actual delivery date` is blank for orders not yet delivered (`In transit`, `Failed to deliver`, `Returned to retailer`). Decide how to treat them; lateness cannot be computed for them.
- Lateness must be derived by comparing `Actual delivery date` to `Expected delivery date`. There is no supplied late flag.
- `Review date &time` falls after the order date, and often after the return. If a review feature is used to predict returns, check the timing or it will leak.
- `table3_delivery_data` holds 14,042 rows for 13,000 distinct `Order ID`s — there are duplicate delivery records. Deduplicate before joining or returns will be double-counted.
- The reviews table covers roughly 30% of orders. Absence of a review is not a neutral signal and should be modelled as its own category rather than imputed.


## Data quality notes

This is an extract from live operational systems and has **not** been cleaned. Expect:

- Missing values in optional / conditionally-populated fields
- Inconsistent casing and stray whitespace in some categorical fields
- A small number of duplicate records
- Occasional out-of-range or implausible values from data-capture errors
- Some date fields captured in inconsistent formats

_Synthetic data supplied for the CAP182 capstone project. Not real client data._
