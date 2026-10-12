-- 1. Insert test customers
INSERT INTO customers (customer_id, name, email) VALUES
(1, 'Sara Ahmed', 'sara@example.com'),
(2, 'Omar Ali', 'omar@example.com'),
(3, 'Emma Hansen', 'emma@example.com'),
(4, 'Adam Noor', 'adam@example.com');

-- 2. Insert test products
INSERT INTO products (product_id, name, price) VALUES
(1, 'Headphones', 499.00),
(2, 'Keyboard', 299.00),
(3, 'Mouse', 149.00),
(4, 'Monitor', 1999.00);

-- 3. Insert test orders
INSERT INTO orders (order_id, customer_id, order_date) VALUES
(1, 1, '2026-10-01'),
(2, 2, '2026-10-02'),
(3, 1, '2026-10-03'),
(4, 3, '2026-10-04'),
(5, 4, '2026-10-05');

-- 4. Connect orders with products
INSERT INTO order_items (order_id, product_id, quantity) VALUES
(1, 1, 1),
(1, 2, 2),
(2, 3, 2),
(3, 4, 1),
(4, 1, 1),
(4, 3, 1),
(5, 2, 1);

-- UPDATE: Change a product's price
UPDATE products SET price = 159.00 WHERE product_id = 3;

-- DELETE: Insert and remove temporary test information 
INSERT INTO customers (customer_id, name, email)
VALUES (99, 'Temporary Customer', 'temp@example.com');

DELETE FROM customers WHERE customer_id = 99;

-- QUERY 1: Show all customers
SELECT * FROM customers;

-- QUERY 2: Find products costing more than 200
SELECT * FROM products WHERE price > 200;

-- QUERY 3: Show orders with customer names
SELECT orders.order_id, customers.name, orders.order_date
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id;

-- QUERY 4: Show products included in each order
SELECT orders.order_id, products.name, order_items.quantity
FROM order_items
JOIN orders ON order_items.order_id = orders.order_id
JOIN products ON order_items.product_id = products.product_id;

-- QUERY 5: Calculate total quantity sold per product
SELECT products.name, SUM(order_items.quantity) AS total_sold
FROM order_items
JOIN products ON order_items.product_id = products.product_id
GROUP BY products.name;

-- QUERY 6: Find products sold more than once
SELECT products.name, SUM(order_items.quantity) AS total_sold
FROM order_items
JOIN products ON order_items.product_id = products.product_id
GROUP BY products.name
HAVING SUM(order_items.quantity) > 1;

-- QUERY 7: Calculate each orders total value
SELECT orders.order_id,
       SUM(products.price * order_items.quantity) AS order_total
FROM orders
JOIN order_items ON orders.order_id = order_items.order_id
JOIN products ON order_items.product_id = products.product_id
GROUP BY orders.order_id;

-- QUERY 8: Find products priced above the normal price
SELECT name, price
FROM products
WHERE price > (SELECT AVG(price) FROM products);