# Django Best Practice

## Setup

The first thing to do is to clone the repository:

```sh
mkdir my_project
cd my_project
git init
git pull https://github.com/mfrony2003/BestPractice-Django.git

```

Create a virtual environment to install dependencies in and activate it:

```sh
py -m venv venv
venv\Scripts\activate.bat
```

Then install the dependencies:

```sh
(venv)$ **pip install -r requirements.txt**

```
Then create .env file  :

```sh
cd config/configSettings
nul > .env [for windown]
touch .env [for linux ]
```

paste the code in the env file

```sh
SECRET_KEY = 'django-insecure-%_poyt*ry%pbv%hq7a2m1=q0j8pvsue_rk9%mui0nj&6*0jobc'

DEBUG=False

PROD_DATABASES_ENGINE =  "django.db.backends.sqlite3"
PROD_DATABASES_NAME =   "db.sqlite3"


LOCAL_DATABASES_ENGINE =  "django.db.backends.sqlite3"
LOCAL_DATABASES_NAME =   "db.sqlite3"
 
```
![config](https://github.com/mfrony2003/BestPractice-Django/assets/26355258/7219e928-fe3c-4368-a8d3-e29614258407)

Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment .


```sh
 cd /my_project 
 py manage.py runserver 
```
And navigate to `http://127.0.0.1:8000/` or 'http://localhost:8000/'


![Home](https://github.com/mfrony2003/BestPractice-Django/assets/26355258/159463fa-88f2-4f88-be66-fb0045fccebf)
