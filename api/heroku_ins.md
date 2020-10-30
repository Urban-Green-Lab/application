# How to deploy DRF to heroku

1. Installations

    ```shell
    $ pip install django-cors-headers
    $ pip install whitenoise
    $ pip install dj_database_url
    $ pip install psycopg2-binary
    $ pip install gunicorn
    ```

1. Add file to hold env variables

    ```py
    # djangoapiproj/hidden_keys.py
    import os

    os.environ['SECRET_KEY'] = {SECRET_KEY}
    ```

1. Heroku env variables

    - Go to settings of heroku application and scoll to Config Vars
    - IS_HEROKU = `True`
    - SECRET_KEY = {SECRET_KEY}

1. Update settings of python application

    ```py
    # Pull in IS_HEROKU to see if in production or not
    is_prod = os.getenv('IS_HEROKU', None)

    # If not in production, pull in Environmental Variables locally
    if is_prod is None:
        import djangorestproj.hidden_keys

    # Pull in secert key from Environmental Variables
    SECRET_KEY = os.getenv('SECRET_KEY')

    CORS_ORIGIN_WHITELIST = (
        "FRONT_END_DOMAIN_URL",
        "LOCALHOST_DOMAIN_URL", # Remove this when development is over
    )

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'djangorestproj', # Django app

        # Add the following
        'rest_framework',
        'corsheaders',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',

        # Add the following
        'corsheaders.middleware.CorsMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',
    ]

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
            # Add the following
            'DIRS': [os.path.join(BASE_DIR, "templates")],
        },
    ]

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.TokenAuthentication',
        ),
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
    }

    # Add this for heroku to collect static files
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

    # Extra places for collectstatic to find static files.
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )

    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    # Heroku needs a postgress database. This establishes it as one if in production.
    # This allows for you to use a nother type of database locally
    if is_prod:
        import dj_database_url
        prod_db = dj_database_url.config(conn_max_age=500)
        DATABASES['default'].update(prod_db)

    ```

- Add Procfile to the root directory to tell heroku commands to run for applicaiton
    ```
    # ./Procfile
    web: gunicorn djangorestproj.wsgi
    release: python manage.py makemigration
    release: python manage.py migrate
    ```
- Add runtime.txt to the root directory to tell heroku what version of python to run
    ```txt
    # ./requirements.txt
    python-3.8.1
    ```
- Log what installations heroku has to make for app to run
    ```shell
    # Run this command
    $ pip freeze > requirements.txt
    ```
- Login to heroku
    ```shell
    $ heroku login
    ```
- Connect Heroku app with local ({HEROKU_GIT_URL} is in Heroku settings)
    ```shell
    $ git remote add heroku {HEROKU_GIT_URL}
    ```
- Disable collectstatic
    ```shell
    $ heroku config:set DISABLE_COLLECTSTATIC=1
    ```
- Add changes and commit them to heroku's github

    ```shell
    $ git add -A && git commit -m "setup for heroku deployment" && git push heroku master
    ```
    - If your api lives in a sub-directory run this command to push up the branch the toplevel of the working tree.
    ```shell
    $ git subtree push --prefix {SUBDIRECTORY_PATH} heroku master
    ```
- Make sure there are both a static/ folder in your api directory and a staticfiles/ folder in your project folder
- Enable collectstatic for future deploys
    ```shell
    $ heroku config:unset DISABLE_COLLECTSTATIC
    ```
- Ensure that at least one instance of the app is running
    ```shell
    $ heroku ps:scale web=1
    ```
- Open the website as follows:
    ```shell
    $ heroku open
    ```
- You will see an error saying that the application is not an allowed host, so you will have to add the new site to your application's settings.
    ```python
    # ./djangorestproj/settings.py
    ALLOWED_HOSTS = [
        # Add Heroku url here
        'HEROKU_DOMAIN_NAME.herokuapp.com',
    ]
    ```
- Add, commit, and push up new changes.

    ```shell
    $ git add -A && git commit -m "updated settings with heroku domain as allowed host" && git push heroku master
    ```

- Check to make sure the warning is gone from deployed app
