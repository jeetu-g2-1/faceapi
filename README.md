# FaceAPI

FaceAPI is a RESTful API built using **Django**, **Django REST Framework**, **MySQL 8**, and deployed with **Nginx**.

---

## 🚀 Tech Stack

- Python 3.12
- Django
- Django REST Framework
- MySQL 8
- Nginx 1.24
- GCC 13.3
- CMake 3.28

---

# 📌 System Prerequisites

Ensure the following packages are installed:

| Software | Version |
|----------|----------|
| Python   | 3.12 |
| MySQL    | 8.x |
| Nginx    | 1.24 |
| GCC      | 13.3 |
| CMake    | 3.28 |
| pip      | Latest |
| venv     | Enabled |

---

# 📌 Packages

Ensure the following packages are installed:

| Package | Version |
|----------|----------|
| django   | 4.2 |
| djangorestframework | 3.16 |
| djangorestframework-api--key | 3.1 |
| dlib      | 20 |
| setuptools | 80 |
| face-recognition | 1.3 |
| gunicorn | 23.0 |
| mysqlclient  | 2.2 |

---

# 🛠 Installation Guide (Ubuntu/Debian)

## 1️⃣ Update System

```bash
sudo apt update
sudo apt upgrade -y
```
## 2️⃣ Install Required Packages

```bash
sudo apt install nginx
sudo apt install mysql-server
sudo apt install python3-pip
sudo apt install python3-venv
sudo apt install python3-dev
sudo apt install build-essential cmake
```


## Make directroy

```bash
mkdir webapi
python3 -m venv apienv
source apienv/bin/activate
```

## Install project dependencies

```bash
pip install -r requirements.txt
```

## mysql database setup

```bash
sudo su -
mysql -u root
create database proctored_exam;
create user 'proctor_admin'@'localhost' identified by 'password';
grant all privileges on procotred_exam.* to 'proctor_admin'@'localhost';
flush privileges;
EXIT;
```

## Make directory of faceapi
 ```bash
mkdir faceapi
git init
git clone project_repository
```


## Django 
> Model migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

> API key creation

```bash
python manage.py createapi
.....
Enter API Key name: faceapi
API Key created successfully!
API Key: ****************************(copy it and keep secure)
Save this key securely. It will not be shown again.
```

## Django modules configuration

> update settings.py

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DATABASE_NAME',
        'USER': 'USER_NAME',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

> Installed apps

```bash
INSTALLED_APPS = [
 'rest_framework_api_key',
 'rest_framework',
 'app_name',
]
```

> Templates

```bash
TEMPLATES=[
{
  'DIRS': [ BASE_DIR / 'templates' ],
}
]
```

> Time Zone

```bash
TIME_ZONE = 'Asia/Kolkata'
```
> Static folder

```bash
import os
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL='/media/'

MEDIA_ROOT=os.path.join(BASE_DIR,'media')
```
> Restframework
```bash
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.authentication.SessionAuthentication',
    ]
}
```

