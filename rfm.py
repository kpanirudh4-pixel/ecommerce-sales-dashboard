import pandas as pd
from sqlalchemy import create_engine

# Connect to MySQL
from urllib.parse import quote_plus

password = quote_plus("@anirudh123")
engine = create_engine(f"mysql+mysqlconnector://root:{password}@127.0.0.1/ecommerce")
# Load data
query = """
    SELECT 
        o.customer_id,
        MAX(o.order_purchase_timestamp) AS last_purchase,
        COUNT(DISTINCT o.order_id) AS frequency,
        ROUND(SUM(p.payment_value), 2) AS monetary
    FROM orders o
    JOIN order_payments p ON o.order_id = p.order_id
    WHERE o.order_status = 'delivered'
    GROUP BY o.customer_id
"""

df = pd.read_sql(query, engine)
print("Data loaded! Shape:", df.shape)

# Calculate Recency (days since last purchase)
import datetime
df['last_purchase'] = pd.to_datetime(df['last_purchase'])
reference_date = df['last_purchase'].max() + datetime.timedelta(days=1)
df['recency'] = (reference_date - df['last_purchase']).dt.days

# Score each metric 1-5 (5 is best)
df['R_score'] = pd.qcut(df['recency'], 5, labels=[5,4,3,2,1])
df['F_score'] = pd.qcut(df['frequency'].rank(method='first'), 5, labels=[1,2,3,4,5])
df['M_score'] = pd.qcut(df['monetary'], 5, labels=[1,2,3,4,5])

# Combine scores
df['RFM_score'] = df['R_score'].astype(str) + df['F_score'].astype(str) + df['M_score'].astype(str)

# Segment customers
def segment(row):
    r = int(row['R_score'])
    f = int(row['F_score'])
    m = int(row['M_score'])
    if r >= 4 and f >= 4 and m >= 4:
        return 'Champion'
    elif r >= 3 and f >= 3:
        return 'Loyal Customer'
    elif r >= 4 and f <= 2:
        return 'New Customer'
    elif r <= 2 and f >= 3:
        return 'At Risk'
    elif r <= 2 and f <= 2:
        return 'Lost'
    else:
        return 'Potential Loyal'

df['segment'] = df.apply(segment, axis=1)

# Summary
print("\nCustomer Segments:")
print(df['segment'].value_counts())

# Save to CSV
df.to_csv(r"C:\Users\DELL\Desktop\DLS\job\project\e commerce project\rfm_results.csv", index=False)
print("\nRFM results saved to CSV!")