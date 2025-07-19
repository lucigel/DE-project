with orders as (
    select * from {{ ref('stg_orders') }}
),

order_items as (
    select * from {{ ref('stg_order_items') }}
),

-- Debug: Kiểm tra xem có bao nhiêu order_items cho mỗi order
order_agg as (
    select 
        o.order_id,
        o.customer_id,
        o.order_date,
        sum(i.total_price) as total_amount,
        count(distinct i.product_id) as num_products
    from orders o
    join order_items i on o.order_id = i.order_id
    group by o.order_id, o.customer_id, o.order_date
),

-- Ensure uniqueness (in case there are still duplicates from joins)
final as (
    select
        order_id,
        customer_id,
        order_date,
        total_amount,
        num_products,
        row_number() over (partition by order_id order by order_date) as row_num
    from order_agg
)

select 
    order_id,
    customer_id,
    order_date,
    total_amount,
    num_products
from final
where row_num = 1