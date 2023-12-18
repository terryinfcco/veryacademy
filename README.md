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
