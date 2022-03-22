# Write your MySQL query statement below
select name as Customers from (select Customers.id, Orders.id as oid, name from Customers
left join Orders on Orders.customerId = Customers.id) as stats
where oid is null