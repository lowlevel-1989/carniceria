## INSTALL ENVIROMENT
~~~
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
~~~

## SETTING DATABASE
~~~
# carniceria/settings.py

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# SQLITE (DEFAULT ONLY DEV)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# POSTGRESQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# OTHER ENGINE
'django.db.backends.postgresql'
'django.db.backends.mysql'
'django.db.backends.sqlite3'
'django.db.backends.oracle'
~~~

## CREATE STRUCTURE DATABASE
~~~
$ python manage.py migrate
~~~

## CREATE SUPER USER
~~~
$ python manage.py createsuperuser
~~~

## RUN SERVER ONLY FOR DEV
~~~
$ python manage.py runserver
~~~


## SUPPORT FILTER IN PRODUCTS
~~~
	http://web.com/?name=sadsa
	http://web.com/?name__contains=fgfdg

	http://web.com/?category__id=1
	http://web.com/>category__name=sadsad
~~~
