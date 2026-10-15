# Version 1 - Raw Implementation
if product["active"] and product["stock"] >= quantity ...

This version directly uses attributes as given in the description


# Version 2 - Named concepts
product_available = product["active"]
enough_stock = product["stock"] >= quantity

## What changed compared with the previous version?
This version creates and stores values in variables that state their purpose for example enough_stock is checking whether there is enough stock vs quantity

## What became easier to understand?
It clearly indicates where the values are stored so it is easier for a developer to trace the rules

## What became easier to change?
It makes it easier to change rules because they can be traced to where they've been stored in the clearly named concepts/variables

## What duplication was removed?
With this version, the developer does not have to repeatedly state the rules for instance in every if condition. the developer can simply use variable names to derive what they've stored

## If a business rule changes later, where would I need to change the code?
If a business rule changed, I would allocate the lines where i assigned the rules to the variables and edit the values
for example, currently, enough_stock = stock >= quantity, if the rules said quantity should not empty the stock, i would change only the value of variabe, making it enough_stock = stock > quantity

## What is the advantage for another developer reading the program?
it gives another developer a clearer view of the rules since they are stored in appropriately named concepts



# Version 3 - Reusable responsibilities
product_available = is_product_available(product)
enough_stock = has_enough_stock(product["stock"], quantity)

## What changed compared with the previous version?
In this version, the developer creates functions to return what a derived variable(calculated from given variables) carrying when called upon and stores it in an appropriately named variable


## What became easier to understand?


## What became easier to change?


## What duplication was removed?


## If a business rule changes later, where would I need to change the code?


## What is the advantage for another developer reading the program?

# Version 4 - Composed business rule
order_proceeds = can_place_order(...)

## What changed compared with the previous version?

This version creates a larger function that checks the validity of other functions in the program in order to make the final decision and stores it in a single variable also known as the composed business rule

## What became easier to understand?


## What became easier to change?


## What duplication was removed?


## If a business rule changes later, where would I need to change the code?


## What is the advantage for another developer reading the program?



# One rule, one place
Imagine the business changes the quantity rule from:

quantity > 0
to:

quantity >= 1 and quantity <= 10
In the refactored version:

### Where should that change be made?
In the refactored version, that change should be made in the function is_valid_quantity when defining what it returns

### What would be the disadvantage if the expression quantity > 0 had been copied into five different places in the program?
That would require a developer to search through code and change each quantity > 0 to quantity >= 1 and quantity <= 10 which is time consuming and prone to errors in case some are missed out when changing




# For each current function, write one sentence describing its responsibility.

## calculate_subtotal()

### Responsibility:
Calculates the subtotal from price and quantity.

### Input:
price, quantity

### Output:
Product(*) of price and quantity

### What should this function NOT be responsible for?




## is_valid_quantity()
### Responsibility:
Checks whether the quantity entered into the system is valid

### Input:
quantity

### Output:
boolean, True or False

### What should this function NOT be responsible for?



## is_product_available()
### Responsibility:
Checks whether the product requested by customer is available/active

### Input:
product
### Output:
boolean, True or False

### What should this function NOT be responsible for?



## has_enough_stock()
### Responsibility:
Checks whether the business has enough stock based on customer's order of quantity

### Input:
stock, quantity

### Output:
boolean, True or False

### What should this function NOT be responsible for?

## is_payment_complete()
### Responsibility:
Checks whether the customer has completed payment or not

### Input:
amount_paid, amount_due

### Output:
boolean, True or False
### What should this function NOT be responsible for?

## can_place_order()
### Responsibility:
Checks whether the customer can place an order or not

### Input:
product_available,valid_quantity,enough_stock,payment_ok

### Output:
True or False

### What should this function NOT be responsible for?



# Program flow

Product details
    ↓
client input data
    ↓
validation of customer input data
    ↓
derived data from calculations of order details  
    ↓
Payment check
    ↓
Order decision
    ↓
Output


## Which parts calculate values?
subtotal
valid_quantity
product_available
enough_stock
payment_ok

## Which parts make decisions?
order_proceeds
requires_manual_review
is_given_discount
gets_free_delivery

## Which parts only display information?
client_order()