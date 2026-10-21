11. Document the data flow
Create:

week-3/tuesday/order-persistence.md
Draw and explain:

Browser
    ↓
POST /order
    ↓
Flask reads input
    ↓
product lookup
    ↓
business functions
    ↓
add_order()
    ↓
SQLite
    ↓
order ID returned
Then:

Browser
    ↓
GET /orders/<id>
    ↓
get_order(id)
    ↓
SQLite
    ↓
order returned
    ↓
Jinja
    ↓
Browser
And then:

payment request
    ↓
update_payment_status()
    ↓
same order row is updated


Please answer briefly:

## Why should add_order() not use request.form directly?
I think it is because it is a database function and not a form field for the user

## Why should the browser not send the subtotal?
It is because the subtotal is a derived value that is got after calculation

## Why does the database create the order ID?
It creates it for easy identification of an order that is saved in sqlite

## Why is the order ID useful between different routes?
It is used to uniquely identify a particular order for get, delete and update requests between routes

## What is the difference between:

get_product(product_id)
This is used to select a single product from the products table

and:

get_order(order_id)
This is used to select a single order from the orders table

## What does commit() do?
I think it saves changes/commits made to sqlite in database.py

## Why does the order still exist after Flask restarts?
It still exists because it is saved in the database, the database exists independent of Flask, thus data persistence

## What happens if we forget to remove one-time insert code from database.py?
If we forget to remove it, then it will run and insert changes each time the database.py file is run
