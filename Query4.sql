SELECT 'Raw' AS version, MIN(price), MAX(price), AVG(price)
FROM listings_raw
UNION ALL
SELECT 'Cleaned', MIN(price), MAX(price), AVG(price)
FROM cleaned_ab_nyc_2019;
