INSERT INTO orders (
    user_id,
    order_date,
    description,
    order_status
)
VALUES (
    %s,
    CURRENT_TIMESTAMP,
    %s,
    'PENDING'
)
RETURNING
    order_id,
    user_id,
    order_date,
    description,
    order_status;