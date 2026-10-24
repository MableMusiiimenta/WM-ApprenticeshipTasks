Write down:

Product:
    id   ---1
    name  ---Filter
    stock  ---3
    price  ---80

Order:
    id      ---1
    product_id ---1
    quantity  ---2
    subtotal  ---160
    payment_amount ---None
Then answer:

Why does an order contain product_id?
It uses it to identify what product was ordered

Can several orders contain the same product_id?
Yes

If product ID 2 appears in three orders, what does that mean?
It means product with ID 2 was ordered thrice

Which table owns the product name and price?
products table

Which table owns the ordered quantity?
orders table


2. Draw the relationship
Create a simple example like:

products

id | name
1  | Filter
2  | Cleaner

orders

id | product_id | quantity
5  | 1          | 2
6  | 2          | 1
7  | 1          | 3

Which orders belong to product 1?
5 and 7

Which orders belong to product 2?
6

How do you know?
Because order id 5 and 7 fall in the same row with product id 1 and order id 6 is in the same row with product id 2



# What I understand now

What connects products and orders?
product id and order id

Why do we store product_id in the order?
To identify which product was ordered in that order

Why does get_orders_for_product() return several rows?
Because it goes through the database and returns all orders with the same product id, which can be more than one

Why does the product route call both get_product() and get_orders_for_product()?
Because it uses get_product() to fetch the product whose orders it's calling

Does the template need to know how SQL works?
No

Why not?
Because the template's functionality is handled in app.py/Flask routing

12. Explain these three lookups
Compare:

## get_product(product_id)
What do I start with?
I start by defining a variable to store the retrieved product details and assigning it to the get_product() function

What am I trying to retrieve?
One product with a particular product_id

Do I expect one result or several results?
One result

## get_order(order_id)
What do I start with?
I start by defining a variable to store the retrieved order details and assigning it to the get_order() function

What am I trying to retrieve?
One order with the specified order id

Do I expect one result or several results?
One result

## get_orders_for_product(product_id)
What do I start with?
I start by defining a variable to store the retrieved orders and assigning it to the get_orders_for_product() function

What am I trying to retrieve?
All orders with the specified product id

Do I expect one result or several results?
One or more depending on how many orders belong to the product



13. Test the complete feature
Test at least:

## existing product with several orders
Input / URL: http://127.0.0.1:5000/products/1
Expected: Display of several orders
Actual: Display of several orders

## existing product with one order
Input / URL: http://127.0.0.1:5000/products/3
Expected: Display one order
Actual: Display one order

## existing product with no orders
Input / URL: http://127.0.0.1:5000/products/2
Expected: "No orders for this product yet"
Actual: "No orders for this product yet"

## product ID that does not exist
Input / URL:  http://127.0.0.1:5000/products/50
Expected: Product does not exist
Actual:  'NoneType' object is not subscriptable, 500 INTERNAL SERVER ERROR
