# Write your MySQL query statement below
SELECT customer_id 
FROM Customer 
group by customer_id
HAVING count( distinct product_key) = (
    SELECT count(*) FROM Product
) 