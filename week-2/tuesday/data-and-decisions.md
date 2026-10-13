# For each variable in your program, write which of those three groups it belongs to and why.

## Raw/input data
customer_is_member  ---this is determined by the company or their system
id  ---this is also assigned by the company or their system
name  ---this is input by the customer
active  ---this is got from the system
stock   ---this is got from the system
price   ---this is got from the system
product  ---this is got from the system
quantity ---this is got from customer input
amount_paid  ---this is got from customer input
country   ---this is got from customer input or location detection(ip adress)


## Derived values
subtotal ---this is got from the multiplying price and quantity
valid_quantity ---this is determined by comparing quantity to 0
product_available  ---this is determined by checking if ctive is True
enough_stock  ---this determined by comparing quantity to stock
payment_ok  ---this is determined by comparing amount paid to subtotal

## Final decisions
requires_manual_review  ---this is decided if subtotal > 500 or quantity > 5 or not payment_ok
order_allowed   ---this is achieved if product_available and valid_quantity and enough_stock and payment_ok
free_delivery  ---this is happens if subtotal >= 100 and country == "DE"
discount_applies  ---this is decided if customer_is_member or subtotal >= 200
