import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://sandali@localhost/olist_dw"
)

tables = [
    "dim_customer",
    "dim_product",
    "dim_seller",
    "dim_date",
    "fact_sales"
]

for table in tables:
    df = pd.read_sql(
        f"SELECT * FROM warehouse.{table}",
        engine
    )

    df.to_csv(
        f"data/processed/{table}.csv",
        index=False
    )

    print(f"{table} exported")