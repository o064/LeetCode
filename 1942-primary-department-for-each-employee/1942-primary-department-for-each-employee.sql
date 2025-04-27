# Write your MySQL query statement below
SELECT employee_id,department_id 
FROM (
    SELECT * ,
    count(employee_id ) over(partition by employee_id ) as depCount
    FROM Employee
) as EmployeesPart
WHERE depCount=1 or primary_flag ='Y'
