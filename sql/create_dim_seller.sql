DROP TABLE IF EXISTS warehouse.dim_seller;

CREATE TABLE warehouse.dim_seller AS

SELECT DISTINCT
    seller_id,
    seller_city,
    seller_state

FROM staging.sellers;