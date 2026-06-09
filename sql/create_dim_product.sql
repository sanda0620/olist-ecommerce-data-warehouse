DROP TABLE IF EXISTS warehouse.dim_product;

CREATE TABLE warehouse.dim_product AS

SELECT
    p.product_id,
    p.product_category_name,
    ct.product_category_name_english,
    p.product_weight_g,
    p.product_length_cm,
    p.product_height_cm,
    p.product_width_cm

FROM staging.products p

LEFT JOIN staging.category_translation ct
ON p.product_category_name = ct.product_category_name;