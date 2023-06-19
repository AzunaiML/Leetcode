select
    case
        when id % 2 = 0 then id -1
        when id = (select max(id) from Seat) and id % 2 = 1 then id
        else id + 1
    end as id,
    student
from Seat
order by 1