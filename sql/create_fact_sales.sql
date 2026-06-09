DROP TABLE IF EXISTS warehouse.fact_sales;

CREATE TABLE warehouse.fact_sales AS

SELECT
    oi.order_id,
    oi.order_item_id,

    o.customer_id,
    oi.product_id,
    oi.seller_id,

    o.order_purchase_timestamp,

    oi.price,
    oi.freight_value,

    ps.total_payment_value,
    ps.payment_installments

FROM staging.order_items oi

JOIN staging.orders o
    ON oi.order_id = o.order_id

LEFT JOIN warehouse.payment_summary ps
    ON oi.order_id = ps.order_id

WHERE o.order_status = 'delivered';