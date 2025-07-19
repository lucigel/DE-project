with source as (
    select * from {{ source('raw', 'raw_orders') }}
)

select
    order_id,
    customer_id,
    to_timestamp(order_date, 'MM/DD/YYYY HH24:MI') as order_date,
    "Country"
from source
where order_id is not null and customer_id is not null
