DROP TABLE IF EXISTS warehouse.dim_date;

CREATE TABLE warehouse.dim_date AS

SELECT
    d::date AS date_key,

    EXTRACT(YEAR FROM d) AS year,

    EXTRACT(QUARTER FROM d) AS quarter,

    EXTRACT(MONTH FROM d) AS month,

    TO_CHAR(d, 'Month') AS month_name,

    EXTRACT(DOW FROM d) AS weekday_number,

    TO_CHAR(d, 'Day') AS weekday_name

FROM generate_series(
    '2016-09-04'::date,
    '2018-10-17'::date,
    interval '1 day'
) d;