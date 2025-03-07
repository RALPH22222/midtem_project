# Django Project Setup Guide

## 1. Create a Project Folder
Navigate to the `htdocs` directory and create a new project folder.

## 2. Set Up a Virtual Environment
Inside your project folder, run:
```sh
virtualenv env
```
Activate the virtual environment:
```sh
env\Scripts\activate  # Windows

## 3. Install Django
```sh
pip install django
```

## 4. Create a Django Project
```sh
django-admin startproject project_name
cd project_name
```

## 5. Run the Development Server
```sh
python manage.py runserver
```

## 6. Create a Django App
```sh
python manage.py startapp app_name
```

## 7. Configure Installed Apps
Open `app_name/apps.py` and copy the class name:
```python
class AppNameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_name'
```
Add the app to `INSTALLED_APPS` in `project_name/settings.py`:
```python
INSTALLED_APPS = [
    ...
    'app_name.apps.AppNameConfig',
]
```

## 8. Configure Templates Directory
In `settings.py`, update the `DIRS` setting:
```python
'DIRS': [
    BASE_DIR / 'templates',
],
```

## 9. Set Up URLs
Inside `app_name`, create a new file `urls.py` and add:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

Update `project_name/urls.py`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_name/', include('app_name.urls')),
]
```

## 10. Set Up the Database (MySQL)
1. Install MySQL client:
   ```sh
   pip install mysqlclient
   ```
2. Update `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_database_name',
           'USER': 'your_username',  
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

## 11. Run Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### Notes:
- You can migrate first, then add fields to Django models later.
- Ensure that views, URLs, and templates are properly updated in your app folder.

This guide provides a structured approach to setting up a Django project with MySQL database integration. Follow these steps carefully to avoid errors.

