import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import psycopg
from psycopg.rows import dict_row

load_dotenv()

app = Flask(__name__)


def get_db_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "webshop"),
        user=os.getenv("DB_USER", "laili"),
        password=os.getenv("DB_PASSWORD", ""),
        row_factory=dict_row
    )


@app.route("/")
def home():
    return jsonify({"message": "Webshop Flask API is running!"})


@app.route("/customers", methods=["GET"])
def get_customers():
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM customers ORDER BY customer_id")
                return jsonify(cur.fetchall())
    except psycopg.Error:
        return jsonify({"error": "Could not retrieve customers"}), 500


@app.route("/customers", methods=["POST"])
def add_customer():
    data = request.get_json(silent=True) or {}

    if not data.get("name") or not data.get("email"):
        return jsonify({"error": "Name and email are required"}), 400

    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO customers (name, email) VALUES (%s, %s) RETURNING *",
                    (data["name"], data["email"])
                )
                return jsonify(cur.fetchone()), 201
    except psycopg.errors.UniqueViolation:
        return jsonify({"error": "Email already exists"}), 409
    except psycopg.Error:
        return jsonify({"error": "Could not add customer"}), 500


@app.route("/customers/<int:customer_id>", methods=["PUT"])
def update_customer(customer_id):
    data = request.get_json(silent=True) or {}

    if not data.get("name") or not data.get("email"):
        return jsonify({"error": "Name and email are required"}), 400

    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """UPDATE customers
                       SET name = %s, email = %s
                       WHERE customer_id = %s
                       RETURNING *""",
                    (data["name"], data["email"], customer_id)
                )
                customer = cur.fetchone()

                if customer is None:
                    return jsonify({"error": "Customer not found"}), 404

                return jsonify(customer)
    except psycopg.errors.UniqueViolation:
        return jsonify({"error": "Email already exists"}), 409
    except psycopg.Error:
        return jsonify({"error": "Could not update customer"}), 500


@app.route("/customers/<int:customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "DELETE FROM customers WHERE customer_id = %s RETURNING *",
                    (customer_id,)
                )
                customer = cur.fetchone()

                if customer is None:
                    return jsonify({"error": "Customer not found"}), 404

                return jsonify({"message": "Customer deleted"})
    except psycopg.Error:
        return jsonify({
            "error": "Could not delete customer. The customer may have existing orders."
        }), 409


@app.route("/products", methods=["GET"])
def get_products():
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM products ORDER BY product_id")
                return jsonify(cur.fetchall())
    except psycopg.Error:
        return jsonify({"error": "Could not retrieve products"}), 500


@app.route("/products", methods=["POST"])
def add_product():
    data = request.get_json(silent=True) or {}

    if not data.get("name") or data.get("price") is None:
        return jsonify({"error": "Name and price are required"}), 400

    try:
        price = float(data["price"])
        if price < 0:
            return jsonify({"error": "Price cannot be negative"}), 400

        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO products (name, price) VALUES (%s, %s) RETURNING *",
                    (data["name"], price)
                )
                return jsonify(cur.fetchone()), 201
    except (ValueError, TypeError):
        return jsonify({"error": "Price must be a number"}), 400
    except psycopg.Error:
        return jsonify({"error": "Could not add product"}), 500


@app.route("/orders", methods=["GET"])
def get_orders():
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT
                        o.order_id,
                        o.order_date,
                        c.name AS customer_name,
                        p.name AS product_name,
                        oi.quantity
                    FROM orders o
                    JOIN customers c ON o.customer_id = c.customer_id
                    JOIN order_items oi ON o.order_id = oi.order_id
                    JOIN products p ON oi.product_id = p.product_id
                    ORDER BY o.order_id
                """)
                return jsonify(cur.fetchall())
    except psycopg.Error:
        return jsonify({"error": "Could not retrieve orders"}), 500


if __name__ == "__main__":
    app.run(debug=True)
