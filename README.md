# Django Best Practice

## Setup

The first thing to do is to clone the repository:

```sh
mkdir my_projject
cd my_projject
git pull https://github.com/mfrony2003/djangoBestPractice.git

```

Create a virtual environment to install dependencies in and activate it:

```sh
py -m venv venv
venv\Scripts\activate.bat
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
cd config/configSettings
nul > .env [for windown]
touch .env [for linux ]
paste the code in the env file

SECRET_KEY = 'django-insecure-%_poyt*ry%pbv%hq7a2m1=q0j8pvsue_rk9%mui0nj&6*0jobc'

DEBUG=False

PROD_DATABASES_ENGINE =  "django.db.backends.sqlite3"
PROD_DATABASES_NAME =   "db.sqlite3"


LOCAL_DATABASES_ENGINE =  "django.db.backends.sqlite3"
LOCAL_DATABASES_NAME =   "db.sqlite3"
 
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment .

Once `pip` has finished downloading the dependencies:

```sh
(venv)>py manage.py runserver 
```
And navigate to `http://127.0.0.1:8000/` or 'http://localhost:8000/'

