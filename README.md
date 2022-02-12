uwsgi --socket localhost:5000 --protocol=http -w appserver.wsgi:app
