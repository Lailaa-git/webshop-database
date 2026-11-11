# Webshop Database
# Database Structure and Third Normal Form (3NF)

The database contains four tables:

- **customers:** `customer_id` is the primary key. `name` and `email` depend on `customer_id`.
- **products:** `product_id` is the primary key. `name` and `price` depend on `product_id`.
- **orders:** `order_id` is the primary key. `customer_id` and `order_date` depend on `order_id`.
- **order_items:** The composite primary key is (`order_id`, `product_id`). `quantity` depends on both columns because it describes how many units of a specific product belong to a specific order.

The tables follow 3NF because non-key columns depend on the key, the whole key, and nothing but the key.

## Index
I created an index on `orders(customer_id)` to improve searches for orders belonging to a customer.
The query plans can change depending on the amount of data. PostgreSQL may use a Bitmap Heap Scan when an index is useful. With a small table, it may choose a Sequential Scan because reading the whole table is cheaper. This is expected behaviour.

## Transaction
The file `02_transaction.sql` demonstrates a transaction.
It creates a customer, an order, and an order item together. These records are related because the order belongs to the customer, and the order item belongs to the order.
The transaction uses `BEGIN` and `COMMIT` to save the changes together.
The script also synchronizes the SERIAL sequences to avoid duplicate key errors.

## Backup and Restore
I created a backup using:

```bash
pg_dump -U postgres -d webshop -F c -f webshop_backup.dump
```

I created a new database and restored the backup:

```bash
createdb -U postgres webshop_restore
pg_restore -U postgres -d webshop_restore webshop_backup.dump
```

I compared the row counts in both databases.

| Table | Original | Restored |
|---|---:|---:|
| customers | 2 | 2 |
| products | 1 | 1 |
| orders | 1 | 1 |
| order_items | 1 | 1 |

The matching row counts confirm that the backup and restore worked.

## Permissions
The file `03_roles_permisitions.sql` creates a limited role called `webshop_reader`.
The role can connect to the database and read data using SELECT. INSERT, UPDATE, and DELETE are denied.

## SQL Files

- `create_tables.sql` — creates the database tables and relationships.
- `populate_and_query.sql` — inserts sample data and runs queries.
- `01_index.sql` — compares query plans and creates an index.
- `02_transaction.sql` — demonstrates a transaction.
- `03_roles_permisitions.sql` — creates a limited database role.

## Screenshots

Screenshots show:
- Query plans before and after creating the index.
- Successful transaction execution.
- Allowed SELECT and denied INSERT/UPDATE/DELETE for the reader role.
- Backup and restore row count comparison.
<img width="161" height="102" alt="Screenshot 2026-11-11 at 15 50 37" src="https://github.com/user-attachments/assets/487d812a-aafc-4da7-901f-0144f1939ab3" />

<img width="174" height="104" alt="Screenshot 2026-11-11 at 15 50 46" src="https://github.com/user-attachments/assets/43956e9d-0504-4f40-b23d-c6b60eea94f3" />

<img width="87" height="139" alt="Screenshot 2026-11-11 at 15 50 56" src="https://github.com/user-attachments/assets/cd06f823-08d0-4691-9d0d-70b5ef1899b1" />


