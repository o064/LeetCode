# Write your MySQL query statement below
WITH emp as (
    SELECT d.name as Department, e.name as Employee  , Salary  ,DENSE_RANK() OVER (PARTITION BY d.name  ORDER BY salary DESC) AS salary_rank
    FROM Employee  e
    JOIN Department d
        ON e.departmentId  = d.id
        )
SELECT Department  ,Employee ,Salary 
FROM emp 
WHERE salary_rank <= 3;
