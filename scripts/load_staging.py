import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://sandali@localhost/olist_dw"
)

files = {
    "customers": "olist_customers_dataset.csv",
    "orders": "olist_orders_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "payments": "olist_order_payments_dataset.csv",
    "products": "olist_products_dataset.csv",
    "sellers": "olist_sellers_dataset.csv",
    "reviews": "olist_order_reviews_dataset.csv",
    "geolocation": "olist_geolocation_dataset.csv",
    "category_translation": "product_category_name_translation.csv"
}

for table_name, file_name in files.items():

    print(f"Loading {table_name}...")

    df = pd.read_csv(f"data/raw/{file_name}")

    df.to_sql(
        table_name,
        engine,
        schema="staging",
        if_exists="replace",
        index=False
    )

    print(f"{table_name} loaded successfully!")

print("All staging tables loaded!")