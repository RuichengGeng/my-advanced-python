## Django rest api developer guide(Ruicheng version)

1. Django command, key in: `django-admin` in cmd, you will see all Django commands
2. Start a new project: go the corresponding dir and key in `django-admin startproject <project name>`. For this case, I just key  in `django-admin startproject drinks`.
3. Double check whether you really start a Django project by key in `python manage.py runserver` under the project directory, click the url and get a Django webpage.
4. In step 3, you will see some warnings: You have 18 unapplied migrations... So just key in `python manage.py migrate`
5. Set superuser information, key in `python .\manage.py createsuperuser`, use the link with a `/admin` after the server url, you can log into the superuser account. It will be just Groups and users. So time to develop our own API.
6. new a `models.py` under `drinks/drinks` folder and define you model. And go to `drink/setting.py` add your model name in `INSTALLED_APPS`. At last apply migration: key in `python manage.py makemigrations drinks` and `python manage.py migrate`
7. To see the added models, you can create a `admin.py` under `drink` folder. Restart the server and you can see the drinks in the admin page, then feel free to change!
8. Start up a rest framework:
   1. Go to  `drink/setting.py` add your `rest_framework`  in `INSTALLED_APPS`
   2. Add `serializers`, this will help define python objects to json
   3. Add end point: Create `views.py` under `drinks`. End points is something that could get information from request.
9. Add more services: CRUD
