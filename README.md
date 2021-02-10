# Django RealTime ToDo app

Django Rest Framework task manager

## Installation

To running the project clone the repository
```bash
https://github.com/BogdanIftoda/yukon.git
```

## Usage

Install the project dependencies:
```bash
pipenv install
```

create a db and add the credentials to settings.py

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
then run
```bash
python manage.py migrate
```
create admin account
```bash
python manage.py createsuperuser
```
then to makemigrations for the app
```bash
python manage.py makemigrations 
```

then again run
```bash
python manage.py migrate
```
to start the development server
```bash
python manage.py runserver
```