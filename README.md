Webshop Database
This database contains a small online shop. The webshop has customers, products, orders, and also products included in each order.
The design i the database contains four tables, which are customers, products, orders, and order_items.

Each table has a primary key, except order_items, which uses a compisute primary key.

One customer can have many orders.

Orders and products have many relations through order_items.

Froeing keys will keep and maintain the relationships and connection between tables.

Constraints ensure that emails are always unique, and the prices can never be a negative number, and the quantities are always above the number zero.