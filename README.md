Database structure and 3nf
The webshop database contains four tables: customers, products, orders, and order_items.
The database follows Third Normal Form. Each table has a primary key, and non-key columns depend on the key. 

Index
I created an index on orders(customer_id) to support queries that search for orders belonging to a specific customer.

Transaction
The file 02_transaction.sql contains a transaction with multiple SQL statements. The transaction inserts a test customer and a test product, then commits the changes together.

Permissions
The file 03_roles_permissions.sql creates a limited role called webshop_reader. It grants permission to connect to the database and read table data using SELECT.

SQL files
* create_tables.sql — creates the database tables and relationships.
* 01_index.sql — compares query plans and creates an index.
* 02_transaction.sql — demonstrates a transaction.
* 03_roles_permissions.sql — creates a limited database role.

GitHub Repository
