with customers as (
    select * from {{ ref('stg_customers') }}
),

orders as (
    select * from {{ ref('stg_orders') }}
),

agg_orders as (
    select
        customer_id,
        count(*) as total_orders,
        min(order_date) as first_order_date,
        max(order_date) as last_order_date
    from orders
    group by customer_id
),

-- Ensure uniqueness at the final level
final as (
    select
        c.customer_id,
        c."Country",
        coalesce(a.total_orders, 0) as total_orders,
        a.first_order_date,
        a.last_order_date,
        row_number() over (partition by c.customer_id order by c.customer_id) as row_num
    from customers c
    left join agg_orders a on c.customer_id = a.customer_id
)

select
    customer_id,
    "Country",
    total_orders,
    first_order_date,
    last_order_date
from final
where row_num = 1