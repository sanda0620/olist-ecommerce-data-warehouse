from db import get_engine

engine = get_engine()

def run_sql(file_path):
    with open(file_path, "r") as f:
        sql = f.read()

    with engine.begin() as conn:
        conn.exec_driver_sql(sql)

    print(f"Executed {file_path}")

if __name__ == "__main__":
    run_sql("sql/create_dim_customer.sql")
    run_sql("sql/create_dim_product.sql")
    run_sql("sql/create_dim_date.sql")
    run_sql("sql/create_dim_seller.sql")
    run_sql("sql/create_payment_summary.sql")

    print("\nDimensions built successfully!")