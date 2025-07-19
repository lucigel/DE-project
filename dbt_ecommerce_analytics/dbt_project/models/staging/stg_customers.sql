with source as (
    select * from {{ source('raw', 'raw_customers') }}
)

select distinct
    customer_id,
    "Country"
from source
where customer_id is not null


