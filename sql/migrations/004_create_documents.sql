CREATE TABLE IF NOT EXISTS documents (
    document_id BIGSERIAL PRIMARY KEY,

    order_id BIGINT,

    document_type VARCHAR(50) NOT NULL,

    file_name VARCHAR(255) NOT NULL,

    s3_key VARCHAR(500) NOT NULL,

    uploaded_at TIMESTAMP NOT NULL,

    CONSTRAINT fk_documents_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
);