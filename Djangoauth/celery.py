from __future__ import absolute_import
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Djangoauth.settings') 

app = Celery('gallery')

app.conf.broker_url = 'redis://localhost:6379/0'  

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

from celery.schedules import crontab

app.conf.beat_schedule = {
    'log-every-5-minutes': {
        'task': 'gallery.tasks.log_to_file',
        'schedule': crontab(minute='*/5'),  
    },
}
app.conf.worker_pool = 'solo'
