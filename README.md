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

# 📌 Installation
> Prerequisites

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

> 📌 Packages

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

## 1 Update System

```bash
sudo apt update
sudo apt upgrade -y
```
## 2 Install Required Packages

```bash
sudo apt install nginx
sudo apt install mysql-server
sudo apt install python3-pip
sudo apt install python3-venv
sudo apt install python3-dev
sudo apt install build-essential cmake
sudo apt install pkg-config
sudo apt install default-libmysqlclient-dev
```
## 3 mysql database setup

```bash
sudo su -
mysql -u root
create database proctored_exam;
create user 'proctor_admin'@'localhost' identified by 'password';
grant all privileges on procotred_exam.* to 'proctor_admin'@'localhost';
flush privileges;
EXIT;
```
> [!WARNING]
> This database name and user password used in django project file - settings.py database configuration.


## 4 Make Parent directroy for project and create virtual environment

```bash
 ~/home $ mkdir parentdir
 ~/home $cd parentdir
 ~/home/parentdir $ python3 -m venv myprojectenv
 ~/home/parentdir $ ls
 myprojectenv
 ~/home/parentdir $ source myprojectenv/bin/activate
 (myprojectenv) ~/home/parentdir $ 
```
> In parent directory, faceapi and virtual environment.




## 5 fork the git repository and clone it.

>Before cloning git repository, generate ssh public and private key.
```bash
(myprojectenv) ~/parentdir $  ssh-keygen -t ed25519 -C "email or purpose of the key"
(myprojectenv) ~/parentdir $  ls ~/.ssh
id_ed25519.pub id_ed25519
(myprojectenv) ~/parentdir $  cat ~/.ssh/id_ed25519.pub
copy the public key and paste ssh key in github repository

```
>clone
 ```bash
(myprojectenv) ~/parentdir $ 
(myprojectenv) ~/parentdir $ git "clone ssh_type repository link"
```

## 6 Install project dependencies

```bash

(myprojectenv) ~/parentdir/projectdir $ cd development
(myprojectenv) ~/parentdir/projectdir/development $ pip install -r requirements.txt
```
**development directory contains required packages and its version for installation. **

## 7 Django 
> Model migrations

```bash
(myprojectenv) ~/parentdir/myprojectdir $ python manage.py makemigrations
(myprojectenv) ~/parentdir/myprojectdir $ python manage.py migrate
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

> Create an administrative user for the project by typing:
```bash
(myprojectenv) ~/parentdir/myprojectdir $ python manage.py createsuperuser

```
**You will have to select a username, provide an email address, and choose and confirm a password.**

>You can collect all of the static content into the directory location that you configured by typing:
```bash
(myprojectenv) ~/parentdir/myprojectdir $ python manage.py collectstatic
```

## 8 Creating systemd socket and service files for Gunicorn

> Socket file

```bash
$ sudo nano /etc/systemd/system/gunicorn.socket
```
> /etc/systemd/system/gunicorn.scoket
```bash
[Unit]
Description=gunicorn daemon for Django project
After=network.target

[Service]
User= username
Group=www-data
WorkingDirectory= /home/username/projectdir
ExecStart=/home/username/projectdir/projectenv/bin/gunicorn \
         --access-logfile - \
         --workers 3 \
         --bind unix:/home/username/projectdir/faceapi.sock \
         projectname.wsgi:application

[Install]
WantedBy=multi-user.target

```
> Service file

```bash
$ sudo nano /etc/systemd/system/gunicorn.service
```

> /etc/systemd/system/gunicorn.service

```bash
[Unit]
Description=gunicorn daemon for Django project
After=network.target

[Service]
User= username
Group=www-data
WorkingDirectory= /home/username/projectdir
ExecStart=/home/username/projectdir/projectenv/bin/gunicorn \
         --access-logfile - \
         --workers 3 \
         --bind unix:/home/username/projectdir/faceapi.sock \
         projectname.wsgi:application

RuntimeDirectory=gunicorn
[Install]
WantedBy=multi-user.target

```
> Start and enable Gunicorn socket

```bash
$ sudo systemctl start gunicorn.socket
$ sudo systemctl enable gunicorn.socket
```

This will create the socket file at /run/gunicorn/gunicorn.sock now and at boot.
When a connection is made to that socket, systemd will automatically start the gunicorn.service to handle.

> Checking for the Gunicorn Socket File
Check the status of the process to find out whether it was able to start:
```bash
$ sudo systemctl status gunicorn.sock
```
You should receive an output like this:

```bash
Output
● gunicorn.socket - gunicorn socket
     Loaded: loaded (/etc/systemd/system/gunicorn.socket; enabled; vendor preset: enabled)
     Active: active (listening) since Mon 2026-03-04 15:05:25 IST; 5s ago
   Triggers: ● gunicorn.service
     Listen: /run/gunicorn.sock (Stream)
     CGroup: /system.slice/gunicorn.socket

Mar 4 15:05:25 django systemd[1]: Listening on gunicorn socket.
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

