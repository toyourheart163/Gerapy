release: python gerapy/server/manage.py migate
web: gunicorn --pythonpath gerapy/server server.wsgi --log-file -
scrapyd: scrapyd -l -

