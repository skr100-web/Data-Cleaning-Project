SELECT 'Raw' AS version, AVG(calculated_host_listings_count), MAX(calculated_host_listings_count)
FROM listings_raw
UNION ALL
SELECT 'Cleaned', AVG(calculated_host_listings_count), MAX(calculated_host_listings_count)
FROM cleaned_ab_nyc_2019;
