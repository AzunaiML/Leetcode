select
    activity_date as day,
    count(distinct user_id) as active_users
from
    Activity
where
    activity_date between  DATE_SUB(cast('2019-07-27' as date), INTERVAL 29 DAY) and cast('2019-07-27' as date)
group by 1