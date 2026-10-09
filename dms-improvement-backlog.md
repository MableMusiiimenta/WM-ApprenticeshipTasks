# DMS issue journal

## Baby Edit Feature

### Observation
The code breaks when I click the edit icon on the babies' table.

### Expected behaviour

When a user clicks the edit icon in the table "all babies", for a particular baby, a form filled with the current details of the particular baby appears
### Actual behaviour

When a user clicks the edit icon in the table "all babies", for a particular baby, the program crashes

### Steps to reproduce

Navigate to the "All babies" table and click the edit icon on one of the babies

### Possible cause
I think the code is unable to reach the else part of the function that displays the form with baby information to be edited

### possible solution
The indentation before the last else needs to be removed

### Why I think this may be a problem
Users will not be able to edit babies' details without the system crashing

### How I noticed it
I clicked to edit a random baby's details from the table containing all babies

### Possible area of the code
In the views.py directly in the edit function

### Questions
How do I go about it?
How do I ensure it does not happen again in future?


# Non-functional links
### Observation
On the dashboard, the links for Supply Inventory, check pending fees payments, bills and invoicing, babies last week, staff schedule and supplies consumed last week are not clickable. They are just words.

### Expected behaviour

When a user clicks the above-mentioned links on the dashboard, she is supposed to go to the respective page or information insinuated in the links.

### Actual behaviour

When a user clicks the above-mentioned links on the dashboard, she stays on the dashboard page and nothing else happens

### Steps to reproduce

Navigate to the dashboard and click the links mentioned in the issue

### Possible cause 

I think it is caused by non-existing pages. The links simply are placeholders.

### possible solution
The pages/information tagged need to be implemented and linked to the dashboard

### Why I think this may be a problem
The administrator might want to click to view those details and fail.

### How I noticed it
I hovered over them and they aren't clickable


### Possible area of the code
This area is the dashb.html template

### Questions


# Hidden Notification
### Observation
The success message after registering baby arrival partly disappears under the navbar

### Expected behaviour

When a user successfully submits the baby's arrival form, the success message displays clearly on a page.

### Actual behaviour

When a user successfully submits the baby's arrival form, the success message is hidden under the navbar and one can't tell what it says.

### Steps to reproduce

Correctly fill a form to register baby's arrival and submit

### Possible cause
I think in the base.html, the body does not have enough top padding to cater for the notification or the notification does not have enough top margin to push it down enough to be viewed

### possible solution
I suggest to increase the top padding for the body

### How I noticed it
I registered new arrival and successfully submitted the details

### Why I think this may be a problem
It's not visible so One might wonder what notification is partially hidden that they are unable to read

### Possible area of the code
html template for registering baby arrival form




### Observation
The form fields look quite ugly, I think they might do with some css

### How I noticed it
I observed them more keenly and they look too basic

### Why I think this may be a problem
Maybe not a problem but sore on the eyes

### Possible area of the code
form html templates




### Observation
The register baby's arrival/departure form accepts for both drop off and pick up time to be exactly the same which does not make sense since the baby has been assigned to a sitter and so stays for a while in the premises

### How I noticed it
I registered new arrival and input same arrival time and same departure time


### Why I think this may be a problem
It just is not right for an admin to be able register that a baby left at the exact same time they arrived yet they were even assigned a sitter for the day

### Possible area of the code
I am not sure but I think it should be a restriction probably under views.py




### Observation
The baby was received at 5pm by the daycare but the system accepts the entry on time period to be Morning

### How I noticed it
I registered new arrival and selected a period that does not match the time input

### Why I think this may be a problem
How can 5 pm be morning period. It is not right

### Possible area of the code
I am not sure about this as well but I think it is also under views.py