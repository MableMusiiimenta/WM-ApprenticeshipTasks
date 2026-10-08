# To run dms locally;

First ensure you have Python installed, in this case v3.12. Verify by running "python --version"

Navigate to the folder where you intend to keep dms, open in terminal and run "git clone https://github.com/MableMusiiimenta/web_app.git" , open your preferred code editor, like VS Code and set up a virtual environment. 

On Ubuntu/Linux, that would be "python3 -m venv venv". The second venv in this case is the name of your virtual environment, which can be any name but it's common courtesy for developers to name it venv too.

Then activate your virtual environment with source venv/bin/activate on Linux.

Install Django into your virtual environment.

Cd into web_app directory

Since the project does not have a requirements.txt or another file for dependencies, simply run it and install them as they are pointed out by the terminal. 

Run the project with "python3 manage.py runserver" . Or use py, python, depending on your OS. After installing the required dependencies, the project will then run successfully.


# DMS architecture map

It is a django MVT framework project. It all starts with the browser sending an HTTP request to the server. Django receives that request, the URL routing determines which view handles it, the view performs the application logic and may use forms/models/database data, and finally Django sends an HTTP response back to the browser. 
The view then operates the function inside it, where it finds the template assigned for the task by the user, which it then renders to the User Interface. The views also save valid data to the database(db.sqlite3) where necessary, if the user inputs or edits data in the forms rendered.


# An example request flow

## The user is adding a new toddler to the system

User clicks the "Add Baby" button, triggering "path("add/", views.add, name="add") under the app's urls.py, which in turn calls upon the view function assigned to it which in this case is "add" function under views.py. The function then runs its code which renders a template, which is an empty form which then displays on the user interface.

User inputs baby data such as name, age, parent's name, parent's contact, etc.

The user clicks submit. Submit still calls upon the urls.py, which in turn calls the "add" view function, which checks the validity of the data entered. 

If it is all valid, the view function runs the save() function to store the details in the database and the updated UI appears because another response/template later reads and displays that data. If anything is invalid, the user gets an error message or notification and the page does not get submitted.


# 3 good things

I like the very strict authentication of the login as it ensures security of the system

I like how the add function operates by adding to what is already existing and then displaying new quantity correctly, in amout paid, supplies, etc.

I like the color combination, it is simple but stands out.

# 3 things I would improve

I would make another login for baby sitters so that they are able to help with tasks like registering babies or items because it could be too much work for one administrator if the babies were so many in number. While also implementing authorization so that parts of the system still only belong to the administrator, like payments.

I would improve on the inventory, the process of when an item has been added or deducted to reflect correctly what is left

i would also add an alert for when the daycare is almost running out of a supply by setting a minimum amount for the admin to stock items on time and the daycare to run smoothly.

# 5 or 6 things I want to understand

Could I have used docker and how and why?

If I were to hand over the system to an actual daycare, how would I do that?

If I were to digitalize parents' payments and paying sitters through the system, how would I go about that?

How can I organize my database and have more control over it?

How could I make security tighter? Or is it supposed to be that way locally

What comments do you have about the UI and how could i have done it better?

# On what I understand better now

Now I understand why I need a requirements.txt or other dependency file because it is unnecessary for another developer to have to first experience errors for them to find out what they are missing when trying to run this project.
I also need to fully test a system and each functionaly added as I build to prevent unnoticed errors.

