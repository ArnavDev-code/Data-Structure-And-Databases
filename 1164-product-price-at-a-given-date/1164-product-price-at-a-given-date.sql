WITH LatestPrices AS (
    SELECT 
        product_id,
        new_price AS price,
        RANK() OVER(PARTITION BY product_id ORDER BY change_date DESC) as rnk
    FROM Products
    WHERE change_date <= '2019-08-16'
)
-- 1. Get the latest price change on or before 2019-08-16
SELECT product_id, price 
FROM LatestPrices 
WHERE rnk = 1

UNION

-- 2. Get products whose first price change happens AFTER 2019-08-16
SELECT product_id, 10 AS price
FROM Products
GROUP BY product_id
HAVING MIN(change_date) > '2019-08-16';
