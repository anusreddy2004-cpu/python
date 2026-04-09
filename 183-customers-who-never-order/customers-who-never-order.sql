# Write your MySQL query statement below
Select name As customers
From Customers
where id Not in (Select customerID From orders);
