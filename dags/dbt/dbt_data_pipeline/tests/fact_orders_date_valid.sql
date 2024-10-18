--  Check to ensure that all the dates are valid
select * 
from {{ ref('fct_orders') }} 
where 
    date(order_date)  > CURRENT_DATE()
    and date(order_date) < '1900-01-01'