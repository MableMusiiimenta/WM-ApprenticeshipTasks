
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

from business import (
    calculate_subtotal,
    is_valid_quantity,
    has_enough_stock,
    is_product_available,
    is_payment_complete,
    
)

from database import get_products, get_product, add_order, get_order, get_orders, add_payment, update_stock, get_orders_for_product
from data import order_intake


@app.get("/")
def home():
    return render_template("index.html")

@app.get("/about")
def about():
    return render_template("about.html")

@app.get("/products")
def all_products():
    products=get_products()
    
    return render_template("products.html", products=products)

@app.route("/order", methods=["GET", "POST"])
def order():

    if request.method == "POST":
        product_id = int(request.form["product_id"])
        product = get_product(product_id)
        product_is_available = is_product_available(product)
        quantity = int(request.form["quantity"])
        country = request.form["country"]

        valid_quantity = is_valid_quantity(quantity)
        product_is_available=product_is_available
        enough_stock = has_enough_stock(product["stock"], quantity)
        subtotal = calculate_subtotal(product["price"], quantity)
        order_intake["subtotal"] = subtotal
        
        payment_amount=None
        order_id = add_order(product_id, quantity, subtotal, country, payment_amount)
        return render_template(
                "payment.html",
                product=product,
                product_id=product_id,
                order_id=order_id,
                quantity=quantity,
                country=country,
                subtotal=subtotal,
                valid_quantity=valid_quantity,
                enough_stock=enough_stock
            )
      
    products=get_products()
    return render_template("order.html", products=products)

@app.route("/payment", methods=("GET", "POST"))
def payment():
    if request.method=="POST":
        order_id = int(request.form["order_id"])
        amount = int(request.form["amount"])

        order=get_order(order_id)
        subtotal=order["subtotal"]
        payment_ok = is_payment_complete(amount, subtotal)
        add_payment(amount, order_id)
        update_stock(order_id)
        return redirect(url_for("order_details", 
                            order_id=order_id,)
        )

    
    return render_template("payment.html")


@app.get("/order_details/<int:order_id>")
def order_details(order_id):
    order=get_order(order_id)
    return render_template("order_details.html", order=order)

@app.get("/orders")
def orders():
    orders = get_orders()
    products = get_products()
    return render_template("orders.html", orders=orders, products=products)

@app.get("/products/<int:product_id>")
def orders_for_product(product_id):
    product = get_product(product_id)
    orders=get_orders_for_product(product["id"])
    if product is None:
        print("Product does not exist")
    return render_template("orders_for_product.html", orders=orders, product=product)


if __name__ == "__main__":
    app.run(debug=True)