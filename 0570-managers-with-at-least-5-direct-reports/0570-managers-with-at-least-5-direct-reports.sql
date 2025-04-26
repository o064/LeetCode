# Write your MySQL query statement below
SELECT m.name
FROM Employee  as m
LEFT  JOIN  Employee as e
    on m.id = e.managerId 
GROUP BY m.id 
HAVING COUNT(e.id) >= 5