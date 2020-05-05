release: python setup.py install && python gerapy/server/manage.py migrate
web: gunicorn --pythonpath gerapy/server server.wsgi --log-file -
web2: scrapyd -l -
