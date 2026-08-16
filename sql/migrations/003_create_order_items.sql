CREATE TABLE IF NOT EXISTS order_items (
    order_item_id BIGSERIAL PRIMARY KEY,

    order_id BIGINT NOT NULL,

    product_name VARCHAR(200) NOT NULL,

    quantity INTEGER NOT NULL,

    unit_price NUMERIC(12, 2) NOT NULL,

    CONSTRAINT fk_order_items_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
);