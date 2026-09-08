SELECT
    processed_order_id,
    order_id,
    extracted_data,
    created_at
FROM processed_orders
WHERE order_id = %s
ORDER BY created_at DESC
LIMIT 1;