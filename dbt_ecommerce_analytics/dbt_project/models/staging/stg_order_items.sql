with source as (

    select * from {{ source('raw', 'raw_order_items') }}

) 

select distinct
    order_id,
    product_id,
    "Quantity" as quantity,
    "UnitPrice" as unit_price,
    "Quantity" * "UnitPrice" as total_price

from source
