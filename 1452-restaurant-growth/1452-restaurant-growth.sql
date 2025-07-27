# Write your MySQL query statement below
WITH  daily_report as (
    SELECT  visited_on ,SUM(amount)  as amount 
    FROM Customer 
    GROUP BY visited_on 
    ORDER BY visited_on desc
)

SELECT dr1.visited_on, SUM(dr2.amount) as amount  , ROUND(AVG(dr2.amount),2) as average_amount 
FROM daily_report as dr1 
JOIN daily_report as dr2 
 ON DATEDIFF(dr1.visited_on, dr2.visited_on) BETWEEN 0 AND 6
GROUP BY dr1.visited_on 
HAVING DATEDIFF(dr1.visited_on, MIN(dr2.visited_on)) = 6
ORDER BY dr1.visited_on 

 
