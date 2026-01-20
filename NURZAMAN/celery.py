from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NURZAMAN.settings')
app = Celery('NURZAMAN')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "ten-time-repeat-count": {
        'task': 'main.tasks.count',
        'schedule': crontab(minute='*/1') #every 1 hour
    }
}


app.conf.beat_schedule = {
    "delete-inactive-users": {
        'task': 'main.tasks.delete_inactive_users',
        'schedule': crontab(hour='*/240')
    }
}