import sqlite3

def get_connection():
    connection = sqlite3.connect("app.db")
    connection.row_factory = sqlite3.Row

    return connection

def create_tables():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            active INTEGER NOT NULL,
            stock INTEGER NOT NULL,
            price REAL NOT NULL
        )
    """)

    # connection.execute("""
    #     DROP TABLE IF EXISTS orders
    # """)

    connection.execute("""
        CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        product_id INTEGER NOT NULL,
        quantity INTEGER NOT NULL,
        subtotal REAL NOT NULL,
        country TEXT NOT NULL,
        payment_amount INTEGER
    )
""")

    connection.commit()
    connection.close()

create_tables()

def add_product(name, active, stock, price):
    connection = get_connection()

    connection.execute(
        """
        INSERT INTO products (name, active, stock, price)
        VALUES (?, ?, ?, ?)
        """,
        (name, active, stock, price),
    )

    connection.commit()
    connection.close()

def get_product(product_id):
    connection = get_connection()   

    product = connection.execute(
        "SELECT * FROM products WHERE id = ?",
        (product_id,),
    ).fetchone()

    connection.close()

    return product

def get_products():
    connection = get_connection()

    products = connection.execute(
        "SELECT * FROM products LIMIT 1000" 
    ).fetchall()

    connection.close()

    return products

def add_order(product_id, quantity, subtotal, country, payment_amount):
    connection = get_connection()

    cursor = connection.execute(
        """
        INSERT INTO orders (product_id, quantity, subtotal, country, payment_amount)
        VALUES (?, ?, ?, ?, ?)
        """,
        (product_id, quantity, subtotal, country, payment_amount),
    )

    order_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return order_id


def get_order(order_id):
    connection = get_connection()

    order = connection.execute(
        "SELECT * FROM orders WHERE id = ?",
        (order_id,),
    ).fetchone()

    connection.close()

    return order

def get_orders():
    connection = get_connection()

    orders = connection.execute(
        "SELECT * FROM orders"
    ).fetchall()

    connection.close()

    return orders

def get_orders_for_product(product_id):
    connection = get_connection()

    orders = connection.execute(
        "SELECT * FROM orders where product_id = ?",
        (product_id,)
    ).fetchall()

    connection.close()

    return orders

def add_payment(payment, order_id):
    connection = get_connection()

    connection.execute(
        """
        UPDATE orders SET payment_amount = ? WHERE id = ?
        """,
        (payment, order_id),
    )
    
    connection.commit()
    connection.close()

def update_stock(order_id):
    order=get_order(order_id)
    product=get_product(order["product_id"])
    new_stock=product["stock"]-order["quantity"]
    connection = get_connection()
    connection.execute(
        """
        UPDATE products SET stock = ? WHERE id = ?
        """,
        (new_stock,product["id"])
    )

    connection.commit()
    connection.close()

def add_product(name, active, stock, price):
    connection = get_connection()

    cursor = connection.execute(
        """
        INSERT INTO products (name, active, stock, price)
        VALUES (?, ?, ?, ?)
        """,
        (name, active, stock, price),
    )

    id = cursor.lastrowid

    connection.commit()
    connection.close()

    return id



# UPDATE table_name
# SET column1 = value1, column2 = value2, ...
# WHERE condition;

# if __name__ == "__main__":
#     create_tables()
    
