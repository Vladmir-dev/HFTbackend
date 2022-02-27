#!/usr/bin/env bash
# start-server.sh
DJANGO_SUPERUSER_USERNAME="admin_username"
DJANGO_SUPERUSER_PASSWORD="choosePassword"
DJANGO_SUPERUSER_EMAIL="admin@gmail.com"
 
(python manage.py makemigrations)
(python manage.py migrate)

if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
   (python manage.py createsuperuser  --username $DJANGO_SUPERUSER_USERNAME --no-input --email $DJANGO_SUPERUSER_EMAIL )

fi
(gunicorn HFT.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3) &
nginx -g "daemon off;"