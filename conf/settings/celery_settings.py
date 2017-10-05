import djcelery
#from celery.schedules import crontab

from .common import *

INSTALLED_APPS += ["djcelery", "kombu.transport.django"]
djcelery.setup_loader()

# CELERY
BROKER_URL = 'django://'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Manila'

# Celery Schedule
CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
# CELERYBEAT_SCHEDULE = {
#    'publish_chapters': {
#        'task': 'apps.stories.tasks.scheduled_book_generation',
#        'schedule': crontab(hour='0'),  # runs every 12 midnight
#    },
# }
