# Write your MySQL query statement below
SELECT m.employee_id , m.name  ,
COUNT(*) as reports_count ,
ROUND(SUM(e.age)/COUNT(*)) as average_age 
FROM Employees m  
JOIN Employees e
    on m.employee_id = e.reports_to 
GROUP BY m.employee_id
order by m.employee_id