# Imagine that the product order checker becomes part of a website.

# Write a short answer in your own words to these questions:

# Where would values such as quantity and country come from on a website?
They would come from user input

# What could send those values to the server?
I think a post request on the site sends the values to the server

# Which part of our Python program represents business logic?
I think while using django framework, the business logic is in the views.py

# Which part of the program is only output?
I think the templates part

# If a user changes quantity from 2 to 5, what data would the server need in order to make a new decision?
I think it would need update/edit data


# Take the order program and identify logic that could later become separate functions.

## subtotal = product["price"] * quantity
### Input: 
price and quantity
### Responsibility:
calculates the product of price multiplied by quantity
### Return value:
product of item price and quantity


## valid_quantity = quantity > 0
### Input:
quantity
### Responsibility:
checks if quantity is valid
### Return value:
returns a boolean of True or False based on whether quantity is greater than 0 or not


## enough_stock = product["stock"] >= quantity
### Input:
stock and quantity
### Responsibility:
checks if there's enough stock based on the quantity requested
### Return value:
returns a boolean


## payment_ok = amount_paid >= subtotal
### Input:
amount_paid and subtotal
### Responsibility:
checks if the amount paid by the customer is equal to or greater than the subtotal
### Return value:
returns a boolean value



