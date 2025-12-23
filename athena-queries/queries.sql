-- Total sales by country
SELECT country, SUM(amount) AS total_sales
FROM sales
GROUP BY country;

-- Partition filtered query
SELECT *
FROM sales
WHERE year = 2025 AND month = 3;
