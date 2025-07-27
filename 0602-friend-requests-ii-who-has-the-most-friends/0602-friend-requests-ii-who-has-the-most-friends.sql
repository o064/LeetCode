# Write your MySQL query statement below
WITH all_ids as  (
    SELECT requester_id  as id 
    FROM RequestAccepted 
    UNION ALL 
    SELECT accepter_id   as id 
    FROM RequestAccepted 
)

SELECT id , COUNT(id) as num 
FROM all_ids
GROUP BY id 
ORDER by num desc
LIMIT 1