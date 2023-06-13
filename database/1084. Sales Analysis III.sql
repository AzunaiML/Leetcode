-- https://leetcode.com/problems/sales-analysis-iii/description/

-- Solution 1
select product_id, product_name
from Product
where
    product_id in (
        select product_id
        from Sales
        group by 1
        having max(sale_date) <= '2019-03-31' and min(sale_date) >= '2019-01-01'
    )

-- Solution 2
select p.product_id, p.product_name
from Product p
join Sales s on p.product_id = s.product_id
group by 1,2
having max(s.sale_date) <= '2019-03-31' and min(s.sale_date) >= '2019-01-01'