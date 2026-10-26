Create a new product through the browser and save it to the database.

The main goal is not just to make the feature work. I want you to think through the complete flow first and decide which responsibility belongs in which part of the application.

For today, assume the user enters sensible data. We will focus more on validation tomorrow.

Plan the feature before coding

Create:

week-4/monday/create-product-plan.md
Before changing the application, answer:

What page or route do we need?
/create_product

Which fields does a product need?
product_name
active
stock
price

Which values will come from the HTML form?
product_id

Which file should receive the browser request?
app.py

Which database function will be needed?
INSERT

What should that database function receive?
The attributes of a product

What should it return?
The values of its columns for each product created

Where should the browser go after the product has been created?
Try to describe the flow before writing code.

For example:

Browser     --user sends a GET request
    ↓
product form  ---server displays the create_product form template
    ↓
POST request   ---user submits the form via a POST request
    ↓
Flask route   ---the server receives user input
    ↓
database function  ---then it runs the database function
    ↓
INSERT product  ---the database function inserts the values of the product into table columns
    ↓
new product ID  ---then it generates a new product_id for the product added
    ↓
redirect   ---with a successful POST request, it then changes routes through redirect
    ↓
product detail page   ---and displays the product detail page for all products including the new product


add_product(...)

Responsibility:
Input:
Result:
Its responsibility should be approximately:

Insert one new product into the products table and return the ID of the newly created product.

Validation questions
Do not try to solve all of them today.

What if name is empty?

What if stock is negative?

What if price contains text?

What if price is negative?

What if stock is empty?

What if active is missing?

What if the same product name is entered twice?
Add any other cases you notice.

Tomorrow we will work specifically on deciding:

what input is acceptable,
where validation belongs,
and what the user should see when input is invalid.
9. Review code style

Before committing, review the Python files you changed.

Please check:

consistent 4-space indentation

spaces around assignments
Prefer:

product = get_product(product_id)
instead of:

product=get_product(product_id)
Also check:

readable blank lines
consistent indentation
readable function calls
no leftover temporary print/debug code unless still needed
The goal is not only working code, but code another developer can read comfortably.

GET /products/new

Test: 
Expected: Form display
Actual: Form display

submit a new product


Test:
Expected: 
Actual:

product is inserted


Test:
Expected:
Actual:

new product ID is returned


Test:
Expected:
Actual:

browser redirects


Test:
Expected:
Actual:

new product detail page opens

Test:
Expected:
Actual:

product appears in /products

Test:
Expected:
Actual:

product still exists after Flask restarts

Test:
Expected:
Actual:


