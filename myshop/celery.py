import os
from celery import Celery


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')


# create an instance of the application.
app = Celery('myshop')

# By setting the CELERY namespace,
# all Celery settings need to include the CELERY_ prefix in their name
app.config_from_object('django.conf:settings', namespace='CELERY')

# look for a tasks.py file in each application directory
app.autodiscover_tasks()
