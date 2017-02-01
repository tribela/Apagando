web: gunicorn --access-logfile=- -b 0.0.0.0:8000 app:app --threads 2
dev: FLASK_APP=app.py FLASK_DEBUG=1 flask run -h 0.0.0.0 -p 8000
