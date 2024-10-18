-- Ensure that there are no negative values in the discount column

select 
    orders.item_discount_amount
from 
{{ ref('fct_orders') }} as orders

where orders.item_discount_amount > 0