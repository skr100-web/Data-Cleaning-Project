SELECT 
  (SELECT COUNT(*) FROM listings_raw) AS raw_rows,
  (SELECT COUNT(*) FROM cleaned_ab_nyc_2019) AS cleaned_rows;
