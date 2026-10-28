BEGIN;

INSERT INTO customers (name, email)
VALUES ( 'Test Customer', 'test@example.com');

INSERT INTO products (name, price)
VALUES ('Test Product', 10.00);

COMMIT;