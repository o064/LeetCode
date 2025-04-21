# Write your MySQL query statement below
SELECT activity_date AS day, COUNT(distinct user_id) AS active_users 
FROM Activity
GROUP BY day
HAVING 
    DATEDIFF('2019-07-27',day) <30 AND DATEDIFF('2019-07-27',day) >=0