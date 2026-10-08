# On a fresh Ubuntu computer, to run DMS;

I would make sure I have Python installed, v3.12 in particular,

I would then navigate to my workspace and clone DMS from github, then create a virtual environment and activate it.

Then I would install Django because it is the framework on which it was built.
I would then run Python3 manage.py runserver which would then run errors and show me which dependencies I need to install, like the Bootstrap datepicker since DMS does not have a dependencies file. 

Then I would run the project successfully after installation.

I would then run python3 manage.py migrate to instantiate the project's database to my computer.

In case of errors, I would read the logs in the terminal to understand what to do to solve them

