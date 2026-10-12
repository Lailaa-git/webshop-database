Webshop Database
This database contains a small online shop. The webshop has customers, products, orders, and also products included in each order.
The design i the database contains four tables, which are customers, products, orders, and order_items.

Each table has a primary key, except order_items, which uses a compisute primary key.

One customer can have many orders.

Orders and products have many relations through order_items.

Froeing keys will keep and maintain the relationships and connection between tables.

Constraints ensure that emails are always unique, and the prices can never be a negative number, and the quantities are always above the number zero.

TEST DATA AND SQL QUERIES FILE
Added a test data using the code INSERT INTO, and then modified the data using the code UPDATE, and removing data using the code DELETE FROM.

The file inlude eight documented SELECT queries , covering filtering, JOINs, aggregate functions , GROUPBY, HAVING, and a subquery.

