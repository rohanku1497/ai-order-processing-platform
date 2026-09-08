INSERT INTO processed_orders (
    order_id,
    extracted_data
)
VALUES (%s, %s)
RETURNING
    processed_order_id,
    order_id,
    extracted_data,
    created_at;