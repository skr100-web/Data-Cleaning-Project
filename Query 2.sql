-- how many cleaned values filled with zeros
SELECT COUNT(*) AS filled_zeros
FROM cleaned_ab_nyc_2019
WHERE reviews_per_month = 0;
