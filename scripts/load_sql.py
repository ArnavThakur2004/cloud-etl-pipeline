import pandas as pd
from sqlalchemy import create_engine

# Read transformed data
df = pd.read_csv("data/cleaned_orders.csv")

# PostgreSQL connection
engine = create_engine(
    "postgresql+psycopg2://postgres:ARX%40@127.0.0.1:5432/salesdb"
)

# Load table
df.to_sql(
    "sales",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully!")
print("Rows loaded:", len(df))