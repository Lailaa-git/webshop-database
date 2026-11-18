# Webshop Database and Flask Application

## Database structure and 3NF

The webshop database contains four tables: customers, products, orders, and order_items.
The database follows Third Normal Form. Each table has a primary key, and non-key columns depend on the key.

## Index

I created an index on orders(customer_id) to support queries that search for orders belonging to a specific customer.

## Transaction

The file 02_transaction.sql contains a transaction with multiple SQL statements. The transaction inserts a test customer and a test product, then commits the changes together.

## Permissions

The file 03_roles_permissions.sql creates a limited role called webshop_reader. It grants permission to connect to the database and read table data using SELECT.

## SQL files

- create_tables.sql — creates the database tables and relationships.
- 01_index.sql — compares query plans and creates an index.
- 02_transaction.sql — demonstrates a transaction.
- 03_roles_permissions.sql — creates a limited database role.

## Flask Application

For this work requirement, I created a Python Flask application that connects to the PostgreSQL webshop database using Psycopg 3.
The application allows users to read, insert, update, and delete customer data. It can also retrieve product information and orders with related customer and product information using SQL JOIN.

### Database connection

The database connection uses environment variables stored in a `.env` file. The `.env` file is not included in the GitHub repository. An `.env.example` file is included to show which settings are needed.

### Application routes

| Route | Method | Description |
|---|---|---|
| `/` | GET | Checks if the application is running |
| `/customers` | GET | Retrieves all customers |
| `/customers` | POST | Adds a new customer |
| `/customers/<customer_id>` | PUT | Updates a customer |
| `/customers/<customer_id>` | DELETE | Deletes a customer |
| `/products` | GET | Retrieves all products |
| `/products` | POST | Adds a new product |
| `/orders` | GET | Retrieves orders with customer and product information |

External values are handled using parameterized SQL queries. The application also includes input validation and error handling.

## Installation and running the application

1. Clone the GitHub repository.
2. Open the project folder in the terminal.
3. Go to the Flask application folder:

   `cd flask_app`

4. Create and activate a virtual environment:

   `python3 -m venv venv`

   `source venv/bin/activate`

5. Install the required packages:

   `pip install -r requirements.txt`

6. Create a `.env` file based on `.env.example` and enter your PostgreSQL database settings.

7. Make sure PostgreSQL is running and the webshop database exists.

8. Start the Flask application:

   `python app.py`

The application will run at:

`http://127.0.0.1:5000`

## GitHub Repository

https://github.com/Lailaa-git/webshop-database

