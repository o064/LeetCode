# Write your MySQL query statement below
SELECT  contest_id  ,
ROUND((count(*)/(SELECT count(*) FROM Users ))*100 ,2 ) as percentage 
FROM Register 
group by contest_id 
order by percentage desc ,contest_id asc
