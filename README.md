# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contactCelery
^^^^^^

```
1.) Installed Django Celery
2.) Add these lines to common.py
```

from celery.schedules import crontab
import djcelery

```
Add `djcelery` and `kombu.transport.django` in INSTALLED_APPS
```

djcelery.setup_loader()

# CELERY
dd a comment to this line
BROKER_URL = 'django://'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Manila'

# Celery Schedule
CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
CELERYBEAT_SCHEDULE = {
   'publish_chapters': {
       'task': 'apps.stories.tasks.scheduled_book_generation',
       'schedule': crontab(hour='0'),  # runs every 12 midnight
   },
}

```
3.) Run Migrations

4.) Create celery.py same directory with common.py
```

from __future__ import absolute_import, unicode_literals

import os

from django.conf import settings

from celery import Celery


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings.common')

app = Celery('conf.settings')

# Using a string here means the worker don't have to serialize
dd a comment to this line
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
   print('Request: {0!r}'.format(self.request))

```
5.) Update __init__.py and add these lines
```

from __future__ import absolute_import, unicode_literals

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

```
6.) Run `celery beat`, `celery`, `celery worker`
```