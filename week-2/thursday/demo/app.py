from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# from flask import Flask, redirect, url_for, render_template, request
# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template("login.html")

# @app.route('/success')
# def success():
#     return "logged in successfully"

# @app.route("/login", methods=["POST", "GET"])
# def login():

#     if request.method == "POST" and request.form["username"] == "admin":
#         return redirect(url_for("success"))

#     return redirect(url_for('index'))

# if __name__ == '__main__':
#     app.run(debug=True)



product = {
    "id": 1,
    "name": "Filter",
    "active": True,
    "stock": 3,
    "price": 80,
}

product1 = {
    "id": 2,
    "name": "Tray",
    "active": True,
    "stock": 5,
    "price": 60,
    }

def calculate_subtotal(price, quantity):
    return price * quantity

def is_valid_quantity(quantity):
    return quantity > 0 < 11
  
def is_product_available(product):
    return product["active"]

def has_enough_stock(stock, quantity):
    return stock >= quantity

def is_payment_complete(amount_paid, amount_due):
   return amount_paid >= amount_due


@app.get("/")
def home():
    return render_template("index.html")

@app.get("/about_us")
def about_us():
    return render_template("about_us.html")

# @app.route("/order")
# def order_product():
#     return render_template("order.html")

@app.route("/order", methods=['GET', 'POST'])
def order():
    
    if request.method=="POST":
        product_is_available=is_product_available(product)
        if product_is_available:

            product_name = request.form["product_name"]
            quantity = int(request.form["quantity"])
            country = request.form["country"]
            
            valid_quantity = is_valid_quantity(quantity)
            enough_stock = has_enough_stock(product1["stock"], quantity)
            subtotal = calculate_subtotal(product1["price"], quantity)
            product["subtotal"] = subtotal

            return render_template("payment.html",
                            product1=product1,
                            product=product,
                            product_name=product_name,
                            quantity=quantity,
                            country=country,
                            valid_quantity=valid_quantity,
                            enough_stock=enough_stock,
                            subtotal=subtotal,
                            product_is_available=product_is_available
                            )

    return render_template("order.html", product=product, product1=product1)

@app.route("/payment", methods=['GET', 'POST'])
def payment():
    if request.method=="POST":
        amount = int(request.form["amount"])
                
        payment_ok = is_payment_complete(amount, product["subtotal"])
        return render_template("payment.html",
            amount=amount,
            product=product,
            product1=product1,
            payment_ok=payment_ok
        )
    return render_template("payment.html", product=product, product1=product1)



if __name__ == "__main__":
    app.run(debug=True)