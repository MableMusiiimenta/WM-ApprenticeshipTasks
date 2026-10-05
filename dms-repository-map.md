# Repository Inventory

web_app/                ---This is the project folder which I created with django startproject web_app

    daystar/            ---This is the configuration folder that holds files that Django automatically generates when you run startproject

        settings.py     ---This is where I configure settings for my project, register apps, timezones, set where to pick static files for images and css, bootstrap            and configure login/logout

        urls.py        ---This is where I put the project's url paths, in my case, I used it to point to the app's urls using "include". It is easier because you can have numerous apps in a project and avoid mixing all their url paths in one file. Keeps the original urls.py smart

    daystarapp/
        migrations/    ---This is where migration files are stored whenever I make migrations after adding or editing the models.py file for the database

        models.py      ---This is where I define fields for the info I want to be stored in the database and also set conditions for inputs, like deciding whether a field can be left null or not

        validators.py  ---Here, I customly define what makes an input valid using Regex, then import each validator to models.py to be used for particular fields appropriately

        views.py       ---This file stores the logic of how a functionality operates when a function is called upon by urls.py

        forms.py       ---This comes about when I decide to use Django forms. The forms.py stores form data so that the form template simply calls upon it to display form data. It is also very crucial because it allows further configuration of field values

        urls.py         ---This stores the app's url paths. The url paths are responsible for pointing out the appropriate view function which in turn operates a given functionality like add, delete, edit.

        templates/      ---This folder stores the app's html files that are to be rendered on the User Interface

            babies/     ---Here, all html files in regards to babies are in this folder. This folder is also crucial because it carries the base file for the whole app

                base.html       ---This file supplies other html files with the html boiler plate and uniform layout css when extended
            dolls/      ---This folder stores all html files to do with dolls like adding a new one, editing details of another or deleting. All those pages are stored under this folder

            sitters/    ---This stores all html files concerned with sitter. Also extends base.html from babies

    staticfiles/        ---This folder carries the make-up and design of the project, it has css and images
        css             ---This carries the styles, colors and color combinations in the project
        images          ---This carries the images for the project which are passed on to the app
    db.sqlite3          ---This is the project's database that was automatically created when I ran migrations the 1st time after starting the app
    manage.py           ---This helps run project commands, like runserver, makemigrations, migrate, etc


    