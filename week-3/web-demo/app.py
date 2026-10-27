
from flask import Flask, request, render_template, redirect, url_for, abort

app = Flask(__name__)

from business import (
    calculate_subtotal,
    is_valid_quantity,
    has_enough_stock,
    is_product_available,
    is_payment_complete,
    
)

from database import add_product, get_products, get_product, add_order, get_order, get_orders, add_payment, update_stock, get_orders_for_product
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

@app.route("/products/new_product", methods=["GET", "POST"])
def new_product():

    if request.method == "POST":
        name = request.form["name"]
        active = request.form.get("is_active") == "1"
        stock = int(request.form["stock"])
        price = int(request.form["price"])

        
        id = add_product(name, active, stock, price)
        return redirect(url_for(
            "product_details",
            id = id,)
        )
    return render_template("new_product.html", name=name, stock=stock, price=price)

@app.get("/product_details/<int:id>")
def product_details(id):
    product = get_product(id)
    if product is None:
        return "Product not found", 404
    return render_template("product_details.html", product=product)

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
    if order is None:
        abort(404)
    return render_template("order_details.html", order=order)

@app.get("/orders")
def orders():
    orders = get_orders()
    products = get_products()
    return render_template("orders.html", orders=orders, products=products)

@app.get("/products/<int:product_id>")
def orders_for_product(product_id):
    product = get_product(product_id)
    if product is None:
            abort(404)
    orders=get_orders_for_product(product["id"])

    
    
    return render_template("orders_for_product.html", orders=orders, product=product)

@app.errorhandler(404)
def not_found(error):
    page_title="Page Not Found"
    return render_template("404.html", error=error, page_title=page_title), 404

if __name__ == "__main__":
    app.run(debug=True)