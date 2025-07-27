# Write your MySQL query statement below
WITH  daily_report as (
    SELECT  visited_on ,SUM(amount)  as amount 
    FROM Customer 
    GROUP BY visited_on 
)

SELECT dr1.visited_on, 
        SUM(dr2.amount) as amount  , 
        ROUND(AVG(dr2.amount),2) as average_amount 
FROM daily_report as dr1 
JOIN daily_report as dr2 
    ON dr2.visited_on BETWEEN DATE_SUB(dr1.visited_on, INTERVAL 6 DAY) AND dr1.visited_on
GROUP BY dr1.visited_on 
HAVING COUNT(DISTINCT dr2.visited_on) = 7
ORDER BY dr1.visited_on 

 
