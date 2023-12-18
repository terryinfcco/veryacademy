# veryacademy
Django Initiation part of the Very Academy Udemy Course

### Set up a virtual environment, installed django, created a project and ran the server to see that it all worked
``` bash
python -m venv venv
source venv/bin/activate
pip install django
django-admin startproject core .
python manage.py runserver

```
### Now create an app for our project called newapp
``` bash
./manage.py startapp newapp
```
- Some tutorials will put the apps inside the project directory /core/newapp, but that's not his preference
``` bash
mkdir ./core/newapp
./manage.py startapp newapp ./core/newapp
```
- Generally apps used to make project easier to manage by creating components

### Registering a Django App
- Need to add our app to the INSTALLED_APPS list in core/settings.py
``` python
"newapp",
```

### More About the Django Development Server
- `./manage.py runserver 8080` is how you change to a different port

### Django Request-Response Cycle
- browser sends request to server, then server grabs url (/about, /help, etc.)
- url then points at a view which grabs a template, static files and stuff from the database to build web page
- web page then gets sent back to the user
- admin page is pre built by Django, but have to `./manage.py migrate` to get it to work
- admin page is at `localhost:8000/admin`

