SELECT
    order_id,
    user_id,
    order_date,
    description,
    order_status
FROM orders
WHERE order_id = %s;