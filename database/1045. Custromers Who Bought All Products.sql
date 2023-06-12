-- https://leetcode.com/problems/customers-who-bought-all-products/

-- Write your MySQL query statement below

select
    c.customer_id
from
    Customer c
    join Product p on c.product_key = p.product_key
group by 1
having count(distinct c.product_key) = (select count(*) from Product)