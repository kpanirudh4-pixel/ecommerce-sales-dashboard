# E-Commerce Sales Intelligence Dashboard

## Overview
An end-to-end data analytics project built on the Brazilian Olist E-Commerce dataset (100K+ orders). The project covers the full pipeline from raw data storage in MySQL to customer segmentation in Python to an interactive Power BI dashboard.

## Tools & Technologies
- **Database:** MySQL
- **Analysis:** Python (Pandas, SQLAlchemy)
- **Dashboard:** Power BI
- **Dataset:** Olist Brazilian E-Commerce (Kaggle)

## Project Pipeline
Raw CSV Data → MySQL Database → Python Analysis → Power BI Dashboard

## Key Features
- Monthly revenue trend analysis across 2016-2018
- Top 10 product categories by revenue
- RFM customer segmentation (96K+ customers)
- Average delivery time analysis by state
- Payment type breakdown
- Top states by order volume

## Customer Segments (RFM Analysis)
| Segment | Count |
|---------|-------|
| Loyal Customers | 28,274 |
| At Risk | 23,234 |
| New Customers | 15,603 |
| Lost | 15,298 |
| Potential Loyal | 7,681 |
| Champions | 6,364 |

## Key Insights
- São Paulo accounts for the highest order volume by far
- Credit card is the dominant payment method (78%)
- Remote states like RR and AP have longer average delivery times
- Beauty and watches are the top revenue-generating categories

## Dashboard Preview
![Dashboard](Powerbi_dashboard.png)

## Files
- `rfm.py` — RFM segmentation script
- `Powebi_dashboard.png` — Power BI dashboard screeshot
- `README.md` — Project documentation

## How to Run
1. Download the Olist dataset from Kaggle
2. Set up MySQL database and run the table creation scripts
3. Run `rfm.py` to generate customer segments
4. Open Power BI Desktop and connect to your MySQL database to recreate the dashboard
