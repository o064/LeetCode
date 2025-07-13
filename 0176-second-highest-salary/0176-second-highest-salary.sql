# Write your MySQL query statement below
select (
    select distinct salary
    from employee e
    order by salary desc
    LIMIT 1 , 1
) as SecondHighestSalary 
