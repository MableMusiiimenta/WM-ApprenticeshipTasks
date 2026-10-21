# What does this return?

# products.get(1)
# What does this return?
It returns all items, in key, value pairs in the dictionary whose key is 1

# products.get(2)
It returns all items, in key, value pairs in the dictionary whose key is 2

# What happens with:

# products.get(999)
It returns None

# What is the difference between:

# products[999]
This returns the items of the product in products whose key/id is 999

# products.get(999)
This sends a get request to the server for the items of the product in products whose key/id is 999

# product = products.get(1)
# print(product["name"])
Filter

# print(product["price"])
80

# print(product["stock"])
3

# Explain in your own words what is happening.
product is a variable storing the items in the dictionary whose key/id is 1.
Then the values are called upon using their keys, i.e, name is key, calling Filter, while using the variable name in which they are stored,product

# When the form is submitted:

# product_id = int(request.form["product_id"])
# Then use that ID to find the product:

# product = products.get(product_id)
# Before writing more code, answer:

# Why is the product ID enough?

# Why shouldn't we trust a price sent by the browser?

# 7. Handle a missing product
# What happens if the browser submits an ID that does not exist?

# Use the result of:

# products.get(product_id)
# to detect this.

# For example, think about:

# if product is None:
#     ...
# Choose an appropriate response.

# You already learned about HTTP status codes, so consider what status code would make sense for a product that does not exist.

# 8. Reconnect the existing order logic
# Once you have the selected product, use its trusted server-side values with the functions from business.py.

# For example, conceptually:

# selected product
#     ↓
# product["price"]
# product["stock"]
#     ↓
# business functions
#     ↓
# results
#     ↓
# template
# Use the business functions you already have.

# Do not integrate lots of new functionality today. The goal is to reconnect what already existed after changing the project structure.

# 9. Test the application
# Please test at least:

# select product 1;
# select product 2;
# valid quantity;
# quantity larger than available stock;
# quantity 0;
# inactive product, if your current business logic handles that;
# invalid/nonexistent product ID if you can trigger it.
# For each test, note:

# Input:
# Expected:
# Actual:
# Result:
# 10. Document the new application structure
# Create:

# week-3/monday/application-structure.md
# Explain briefly:

# What does app.py own?

# What does business.py own?

# What does data.py own?

# What do the templates own?

# What does static/ contain?

# Then answer:

# If the rule for valid quantity changes tomorrow, where would I change it?

# If the price of Filter changes tomorrow, where would I change it?

# If the order page needs another heading, where would I change it?

# If we later replace data.py with a database, which parts of the application should ideally need the least change?

# 11. Important persistence note
# Please also write down the difference between:

# shared in-memory data
# and:

# persistent data
# The products dictionary can be shared by different requests while the Flask process is running.

# But it is not persistent storage.

# If Flask restarts, changes made only in memory are lost.

# We will return to this when we introduce database-backed data.

# 12. If you finish early
# Add a second page:

# /products
# that displays all products.

# Use the same products dictionary from data.py.

# This means both:

# /products
# and:

# /order
# use the same server-side product data.

# Do not copy the product dictionary into both routes.

# The point is to have one shared source of product data.

# End-of-day update
# Please send me:

# Done:
Finished the new project structure
Added several products to data.py
Practiced accessing the product dictionary
Handled a missing product
Reconnected the existing order logic
Tested the application
Documented the new application structure
Added a second page, /products

# Learned:
To access a nested dictionary
To separate/organize files according to their roles
To import functions to be used by another file
To loop over an array in Jinja

# Blocked:
Not yet

# Questions:
Not yet

# Documentation used: 
None Today

# AI used: 
None

# One thing I understand better about nested dictionaries: 
I understand that a key of a nested dictionary can work as its unique ID

# One thing I understand better about .get(): 
I understand that it picks out the values of a particular item corresponding to the ID or other unique attribute used to fetch the data

# When would I use .get() instead of a for loop? 
I would use .get() to pick out a particular item in array while I would use a for loop to iterate in sequence over the items in an array

# One thing I understand better about separating app.py, business.py, and data.py:
Separating those files makes the project modular. It makes it easy to trace code since a developer knows that app.py keeps the code for route handling, business.py keeps the business logic of the program and data.py is where the server pre-set info is stored

# One question I still have about shared data or persistence:


# Plan for tomorrow: 
I am looking forward to learning about data persistence