# Write your MySQL query statement below
SELECT p.product_id ,IFNULL(ROUND(SUM(p.price*s.units)/SUM(s.units),2),0) AS average_price 
FROM Prices as p
LEFT JOIN UnitsSold as s
    ON s.product_id = p.product_id    
     AND s.purchase_date BETWEEN p.start_date AND p.end_date 
GROUP BY p.product_id 
 