CREATE TABLE IF NOT EXISTS shipments (
    shipment_id BIGSERIAL PRIMARY KEY,

    order_id BIGINT NOT NULL,

    delivery_date TIMESTAMP,

    status VARCHAR(50) NOT NULL,

    CONSTRAINT fk_shipments_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
);