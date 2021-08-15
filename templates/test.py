[program:fakturakollen-server]
command=/home/azagent/fakturakollen/env/bin/gunicorn --bind 127.0.0.1:8000 src.wsgi
user=azagent
autostart=True
redirect_stderr=true
stdout_logfile=/home/azagent/fakturakollen/logs/fakturakollen.log
environment=DJANGO_SETTINGS_MODULE='src.prod';HTTPS=1
directory=/home/azagent/fakturakollen

[program:fakturakollen-beat]
command=/home/azagent/fakturakollen/env/bin/celery -A src beat --scheduler django_celery_beat.schedulers:DatabaseScheduler
user=azagent  
autostart=True
redirect_stderr=true
stdout_logfile=/home/azagent/fakturakollen/logs/celery_beat.log
environment=DJANGO_SETTINGS_MODULE='src.prod';HTTPS=1
directory=/home/azagent/fakturakollen

[program:fakturakollen-worker]
command=/home/azagent/fakturakollen/env/bin/celery -A src worker -l info -P gevent
user=azagent  
autostart=True
redirect_stderr=true
stdout_logfile=/home/azagent/fakturakollen/logs/celery_worker.log
environment=DJANGO_SETTINGS_MODULE='src.prod';HTTPS=1
directory=/home/azagent/fakturakollen