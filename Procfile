release: python3 manage.py makemigrations && python3 manage.py migrate
web: gunicorn rewardly.wsgi --log-file -
