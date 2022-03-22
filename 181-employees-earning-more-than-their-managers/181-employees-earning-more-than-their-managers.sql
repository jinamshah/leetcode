# Write your MySQL query statement below
select e1name as Employee from (select e1.name as e1name, e1.salary as e1sal, e2.name as e2name, e2.salary as e2sal from Employee as e1
join Employee as e2 on e1.managerId = e2.id) as temp
where e1sal > e2sal;