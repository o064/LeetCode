# Write your MySQL query statement below
SELECT  product_name , SUM(unit) as unit
FROM Products as p 
JOIN Orders as o 
ON p.product_id = o.product_id
WHERE 
    YEAR(o.order_date) = 2020 
    AND MONTH(o.order_date) = 2
group by  product_name       
having  SUM(unit)>=100