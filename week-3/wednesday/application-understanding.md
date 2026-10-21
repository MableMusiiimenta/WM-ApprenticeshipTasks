
Describe these parts in one sentence each:

app.py  ---This is where http route handling takes place
business.py  ---This stores the program's business logic
database.py  ---This is where database functions are run
templates   ---This folder stores html/jinja files
SQLite database ---This is the database where the program's data is stored persistently


Name: get_product()
Responsibility: This function retrieves one stored product using its ID.
Input: product_id
Result/change: It returns the order under the corresponding product_id


Name: get_products()
Responsibility: This function can retrieve all products in the products table, and can also folow a condition set to select products to be retrieved
Input: ()
Result/change: It displays the products, if called to display


Name: add_order()
Responsibility: This function stores an order into the table, orders
Input: product_id, quantity, subtotal, country, payment_amount
Result/change: A new order is inserted into the orders table


Name: get_order()
Responsibility: This function retrieves one stored order using its ID
Input: order_id
Result/change: It returns the order under the corresponding order_id


Name: add_payment()
Responsibility: This function stores a payment into the table, orders, by updating the existing payment_amount which is "None" before submitting the payment form with amount
Input: payment, order_id
Result/change: The column value for Payment_amount becomes an int, entered by the user,  instead of None


Name: calculate_subtotal()
Responsibility: This function calculates an order's subtotal using a product's price and quantity
Input: Price and Quantity
Result/change: Product of Price * Quantity

Name: def order()
Responsibility: This function renders the order input form to the customer through a GET request receives customer input through a POST request, which it then proceeds to save to the database
Input: product_id, product, product_is_available, quantity, country
Result/change: A new order is added to the orders table

Name: def payment()
Responsibility: This function renders the payment input form to the customer through a GET request receives customer input through a POST request, which it then proceeds to save to the database
Input: order_id, amount 
Result/change: the Payment Amount column is updated by the user input



## document what currently happens when a customer:

opens the order page;
chooses a product and quantity;
submits the order;
an order is stored;
later submits a payment.
Draw the flow in a simple form such as:

Browser
    ↓
Flask route
    ↓
Business logic
    ↓
Database function
    ↓
SQLite
    ↓
Template / response
Adapt it to what your application actually does.

4. Review whether each route has one clear responsibility

## @app.get("/")
What user action or page is this route responsible for?
This is responsible for displaying the home page to the user via a GET request

Which template should this route normally display?
index.html

Is this route doing work that belongs to another route?
No

## @app.get("/about")
What user action or page is this route responsible for?
This is responsible for displaying the about us page to the user via a GET request

Which template should this route normally display?
about.html

Is this route doing work that belongs to another route?
No

## @app.get("/products")
What user action or page is this route responsible for?
This is responsible for displaying all products in the products table to the user via a GET request

Which template should this route normally display?
products.html

Is this route doing work that belongs to another route?
Not exactly, it is getting all products using the get_products() database.py function


## @app.route("/order", methods=("GET", "POST"))
What user action or page is this route responsible for?
This is responsible for displaying the order form to the user via a GET request and receiving user input via a POST request

Which template should this route normally display?
order.html

Is this route doing work that belongs to another route?
No

## @app.route("/payment", methods=("GET", "POST"))
What user action or page is this route responsible for?
This is responsible for displaying the payment form to the user via a GET request and receiving user input via a POST request

Which template should this route normally display?
payment.html

Is this route doing work that belongs to another route?
No


## @app.get("/orders/<int:order_id>")
What user action or page is this route responsible for?
This is displaying an order derived from the orders table via order_id

Which template should this route normally display?
order_details.html

Is this route doing work that belongs to another route?
No



What does the /order route currently do?
It is responsible for displaying the order form to the user via a GET request and receiving user input via a POST request

Why is payment.html being rendered there?
It is being rendered after a successful post request for the user to proceed to make payment

Does ordering a product and viewing/paying an existing order represent the same responsibility?
No

How could those responsibilities be separated?
Ordering a product uses the order() function and receives feedback via POST request while viewing/paying an existing order uses the database.py get_order() function using an existing order_id.



@app.get("/order/<int:order_id>")


What information does Flask receive from this URL?
It receives order_id

Which database function do we already have that could use this information?
get_order(order_id)

What should happen if the order exists?
The order should be retrieved and its contents displayed

What should happen if it does not exist?
It should raise a 404, not found status code

Which template should display the order?
order_details.html


7. Test direct order URLs
Create at least two orders.

Then test:

/order/1
Request:
GET

Expected result:
Display order details for order with id 1

Actual result:
Displays order details for order with id 1

/order/2
Request:
GET

Expected result:
Display order details for order with id 2

Actual result:
Displays order details for order with id 2

/order/9999
Document:
Request:
GET

Expected result:
None, order not found, 404

Actual result:
None



9. Explain the difference between rendering and redirecting
Whether or not you implement the optional task, explain:

render_template()
This shows the html template assigned for that function
versus:

redirect()
This changes direction and shows a different html template based on a met condition

Does rendering a template change the browser URL?
No

Does redirecting cause another HTTP request?
Yes

Why might /order rendering payment.html be conceptually confusing even if it technically works?
It might be confusing because the order() function is normally expected to render order.html but instead renders payment.html
