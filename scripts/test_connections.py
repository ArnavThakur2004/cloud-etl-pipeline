from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:ARX@@127.0.0.1:5432/salesdb"
)

with engine.connect() as conn:
    print("Connected successfully!")