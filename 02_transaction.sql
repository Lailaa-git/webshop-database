SELECT setval(
    pg_get_serial_sequence('customers', 'customer_id'),
    COALESCE((SELECT MAX(customer_id) FROM customers), 1),
    EXISTS (SELECT 1 FROM customers)
);
SELECT setval(
    pg_get_serial_sequence('orders', 'order_id'),
    COALESCE((SELECT MAX(order_id) FROM orders), 1),
    EXISTS (SELECT 1 FROM orders)
);
BEGIN;
WITH new_customer AS (
    INSERT INTO customers (name, email)
    VALUES (
        'Transaction Test Customer',
        'transaction.test.' || to_char(clock_timestamp(), 'YYYYMMDDHH24MISSMS') || '@example.com'
    )
    RETURNING customer_id
),
new_order AS (
    INSERT INTO orders (customer_id)
    SELECT customer_id FROM new_customer
    RETURNING order_id
)
INSERT INTO order_items (order_id, product_id, quantity)
SELECT new_order.order_id, products.product_id, 2
FROM new_order
CROSS JOIN (
    SELECT MIN(product_id) AS product_id FROM products
) AS products
WHERE products.product_id IS NOT NULL;

COMMIT;