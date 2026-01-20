from celery import shared_task
from django.conf import settings
from django.db import transaction
from .models import Object, Apartment
from accounts.models import User
from datetime import timedelta
from django.utils import timezone

@shared_task
def count():
    i = 0
    while i < 10:
        i += 1
        print(i)
    print(f'total: {i}')


@shared_task
def delete_inactive_users():
    shutdown_date = timezone.now() - timedelta(days=30)
    only_active_users = User.objects.filter(last_login__lt=shutdown_date)

    for cleaner in only_active_users:
        cleaner.is_active = False
        cleaner.save()