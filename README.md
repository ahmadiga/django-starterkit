# django Starterkit
A simple Django starter-kit with the basic component.

## Requirments
- Docker: https://docs.docker.com/engine/installation/
- Docker-compose: https://docs.docker.com/compose/install/

## Getting Started
1. Dlone/Download the repo:
`git clone --depth 1 https://github.com/ahmadiga/django-starterkit.git`
2. navigate to django-starterkit => docker-build
`cd django-starterkit/docker-build/`
3. build docker containers
`docker-compose build`
4. Launch containers:
`docker-compose up -d`
5. Migrate DB
`docker-compose.exe exec server python manage.py migrate`
6. All done,open your browser and navigate to `http://localhost:8000/`

## What's included
1. Django 2.0.2: https://docs.djangoproject.com/en/2.0/
2. Django Channels 2.0.2: http://channels.readthedocs.io/en/stable/
3. Django anymail 1.4: http://anymail.readthedocs.io/en/stable/
4. Django Compressor 2.2 with sass support using node-sass: https://django-compressor.readthedocs.io/en/latest/
5. Django Crispy Forms 1.7.0: http://django-crispy-forms.readthedocs.io/en/latest/
6. Django Debug Toolbar 1.9.1: https://django-debug-toolbar.readthedocs.io/en/stable/
7. Django NPM 1.0.0: https://github.com/kevin1024/django-npm
8. Django Parsley 0.7: https://github.com/agiliq/Django-parsley
9. Celery 4.1.0 with redis 2.10.6: http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html
10. django-generator 0.01: https://github.com/ahmadiga/django-generator
11. django-allauth 0.35.0: http://django-allauth.readthedocs.io/en/latest/