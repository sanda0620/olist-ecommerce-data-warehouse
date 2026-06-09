DROP TABLE IF EXISTS warehouse.dim_customer;

CREATE TABLE warehouse.dim_customer AS

SELECT DISTINCT
    customer_id,
    customer_unique_id,
    customer_city,
    customer_state

FROM staging.customers;