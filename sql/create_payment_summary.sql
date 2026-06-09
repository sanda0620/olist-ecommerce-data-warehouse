DROP TABLE IF EXISTS warehouse.payment_summary;

CREATE TABLE warehouse.payment_summary AS

SELECT
    order_id,
    SUM(payment_value) AS total_payment_value,
    MAX(payment_installments) AS payment_installments
FROM staging.payments
GROUP BY order_id;