# Write your MySQL query statement below
select e.name AS employee
from employee e
JOIN employee m
On E.MANAGERID=M.ID
where e.salary> m.salary
  