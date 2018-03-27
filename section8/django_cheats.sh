# Cheat sheet to get started on a ~ new ~ django project!
# Creating a new virtual environment

$ virtualenv --python=/usr/local/bin/python3.6 venv
$ source venv/bin/activate
$ pip install Django==2.0.3 
# pip install any other dependencies here, or if you are using requirements.txt 
# skip line 6.

# Create a django project
$ django-admin startproject projectname
$ cd projectname

# Create a django app
$ python manage.py startapp appname

# Create login for the admin
$ python manage.py createsuperuser

# Shell for Django models, etc
$ python manage.py shell

# View SQL statements for a particular migration
$ python manage.py sqlmigrate appname 000x

# Create the SQL migration, and then apply it
$ python manage.py makemigrations
$ python manage.py migrate
