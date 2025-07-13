# Write your MySQL query statement below
DELETE p2 FROM Person p1 
join person p2
    on p2.email = p1.email and p1.id < p2.id

