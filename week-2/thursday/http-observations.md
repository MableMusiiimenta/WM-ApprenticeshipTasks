# what type Flask gives you from the form
string

# why you might need to convert it
It needs to be converted in order to be used in further calculations and validations, for example, the greater than expression is not supported between instances of string and integer

# what could happen if conversion fails
the program returns the string value but will not be able to validate whether quantity is greater than 0, or involve it in any calculations since it is a string value


Open Browser Developer Tools → Network.

Please inspect:

# loading the Home page
## request method
GET
## URL
http://127.0.0.1:5000/
## status code
200


# loading the CSS file
## request method
GET
## URL
http://127.0.0.1:5000/static/style.css
## status code
304


# loading the About page
## request method
GET
## URL
http://127.0.0.1:5000/about_us
## status code
200


# loading the Order page
## request method
GET
## URL
http://127.0.0.1:5000/order
## status code
200


# submitting the form
## request method
POST
## URL
http://127.0.0.1:5000/app
## status code
200


## which request loads the CSS
get request

## which request submits the form
Post request


## Why do we use base.html?
To share common elements to different pages without repeatedly creating them on each html template

## Why do we use Header and Footer partials?

## What is the difference between templates/ and static/?
The templates folder stores html files, while static contains files that Flask sends without rendering them

## What happens when the browser requests /order?
A GET request is sent to the server, which then displays the order page

## What happens after the user submits the form?
A POST request is sent to the server to receive the data

## What does Flask do?
Flask supports other requests, since without it, the browser is only able to receive GET requests. So with Flask, the user is bale to Post data in a form

## What does the browser do?
It receives requests and sends them to the server. It also provides dev tools to inspect the status of the site

USER
 │
 │ enters quantity
 ▼
HTML FORM
 │
 │ POST /order
 ▼
FLASK ROUTE
 │
 │ reads + converts input
 ▼
BUSINESS FUNCTIONS
 │
 ├── is_valid_quantity()
 ├── has_enough_stock()
 └── calculate_subtotal()
 │
 │ results
 ▼
JINJA TEMPLATE
 │
 │ HTML response
 ▼
BROWSER
