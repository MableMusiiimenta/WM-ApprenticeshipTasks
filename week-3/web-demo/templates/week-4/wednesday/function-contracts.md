Function parameters and responsibilities

Create:

week-4/wednesday/function-contracts.md
For these functions:

add_product()
Responsibility: it creates a new product in the products table
Parameters: 
What each parameter represents:
name ---this represents product name
price ---this is the price of the product
stock ---this is the stock amount for the product
active  ---this tells whether the product is available for sale or not

Return value:  ---id
What data this function changes, if any: ---it adds another product to the products table

update_product()
Responsibility: it updates the fields of an already existing product
Parameters:
What each parameter represents:
id  ---this represents the id of the product to be updated
name ---this represents product name
price ---this is the price of the product
stock ---this is the stock amount for the product
active  ---this tells whether the product is available for sale or not


Return value:
What data this function changes, if any:  it changes the field value of the product updated
For update_product(), also map the SQL placeholders.
name = ?       → name
price = ?      → price
stock = ?      → stock
active = ?     → active
WHERE id = ?   → product_id
Then explain:

Why must the number of supplied SQL values match the number of ? placeholders?
Because each placeholder is meant to be filled by each supplied SQL value

Why does their order matter?
Because the function fills in values in sync with the order of the SQL values

What is the difference between a function parameter and the value passed to that parameter?
A function parameter is found in the definition of the function while the value is the value of the parameter

Why are those parameter names available inside the function?
The parameter names are inside the function to let the function know what it is going to use to operate

get_product()
Responsibility: It retrieves an existing product from the products table by product_id
Parameters: product_id
What each parameter represents: product_id  ---this is the id of the product being retrieved
Return value: product
What data this function changes, if any: It doesn't change anything

get_orders_for_product()
Responsibility:  ---it retrieves orders of an existing product
Parameters: product_id
What each parameter represents: product_id is the id of the product whose orders are being retrieved
Return value: orders
What data this function changes, if any: ---It doesn't change anything



Test all three states

Test:

create product
    → created message   ---Displays flash message, "product added successfully" with product details

edit product
    → updated message   ---Displays flash message, "product updated successfully" with product details

directly open product detail URL
    → no message     ---Displays just product details with no flash message
Also refresh the detail page and observe whether the flash message appears again.

On refresh, the flash message does not appear again, because it's a direct GET request for just the details page

