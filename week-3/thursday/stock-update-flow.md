Please explain this flow in your own words:

What information do I have?
What information do I need next?
Where can I get it?


order_id
    ↓
retrieve the order    ---Here i have the order_id, I need the full order details, I can get them from the orders table
    ↓
get product_id from the order  ---I have the full order, i need the product_id, i can get it as an attribute from order's details
    ↓
get quantity from the order   ---I have the full order, i need the quantity, i can get it as an attribute from order's details
    ↓
retrieve the product   ---i have the product_id, i need to retrieve the product, i can get it from the products table 
    ↓
get current stock   ---i have the full product details, i need product stock, i can get it from the product's table
    ↓
calculate new stock  ---i have current stock, and i have order quantity. i need new stock, i can get it from subtracting order quantity from product stock
    ↓
update the product in the database  ---i have the stock column in the products table, i need to update it after an order. i can update it by querying the database using UPDATE




Why is the order ID enough to start this process?
It is enough because it retrieves the full order which also carries product_id as an attribute

Why do we not need the browser to send the product ID again?
Because we already have it as an attribute of an order

Why do we not need the browser to send the quantity again?
Because we already have it as an attribute of an order

Which stored record is the source of truth for the ordered quantity?
the quantity column in the orders table

Which stored record is the source of truth for current stock?
the stock column in the products table

What would happen if the order ID does not exist?
a 404, order does not exist

Write one example with numbers

For example:

order_id = 4

order 4:
    product_id = 2
    quantity = 3

product 2:
    current stock = 10
Then explain:

new stock = 10 - 3 = 7
New stock is the result of order quantity subtracted from product current stock

the database record to be updated is current stock

