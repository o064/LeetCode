# Write your MySQL query statement below
SELECT s.user_id , 
ROUND(
    IFNULL(SUM(c.action = 'confirmed')/COUNT(action),0),
    2) 
    as confirmation_rate
FROM Signups as s
LEFT JOIN  Confirmations c
    on s.user_id = c.user_id 

GROUP BY s.user_id 
