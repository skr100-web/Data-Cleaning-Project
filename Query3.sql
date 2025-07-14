-- Look at the max night for the raw data and 
-- how insane that is with the cleaned one its more accurate


SELECT 'Raw' AS version, MIN(minimum_nights), MAX(minimum_nights), AVG(minimum_nights)
FROM listings_raw
UNION ALL
SELECT 'Cleaned', MIN(minimum_nights), MAX(minimum_nights), AVG(minimum_nights)
FROM cleaned_ab_nyc_2019;
