CREATE TABLE IF NOT EXISTS orders (
    order_id BIGSERIAL PRIMARY KEY,

    user_id BIGINT NOT NULL,

    order_date TIMESTAMP NOT NULL,

    description VARCHAR(500),

    order_status VARCHAR(50) NOT NULL,

    CONSTRAINT fk_orders_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
);