from flask import Flask, request, render_template

app = Flask(__name__)


def is_valid_quantity(quantity):
    return quantity > 0


@app.get("/")
def home():
    return render_template("index.html")

@app.get("/about_us")
def about_us():
    return render_template("about_us.html")

@app.get("/order")
def order_product():
    return render_template("order.html")

@app.post("/app")
def order():
    product_name = request.form["product_name"]
    quantity = int(request.form["quantity"])
    country = request.form["country"]
    if is_valid_quantity(quantity):
        
        return f"Quantity {quantity} is valid for {product_name}. Customer comes from {country}"

    return "Please enter a valid quantity", 404



if __name__ == "__main__":
    app.run(debug=True)