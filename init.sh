#!/bin/bash

if [ -d ~/django_mysql/ ]; then
    mv ~/django_mysql/ ~/web
else
   echo "no path"
fi


if [ -d ask/ ]; then
    echo "ask"
else
   django-admin startproject ask
   cd ask
   ./manage.py startapp  qa
   #python manage.py migrate
fi


sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/main.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/main.conf
sudo /etc/init.d/gunicorn restart

#gunicorn -b 0.0.0.0:8080 hello --chdir ~/web/etc

