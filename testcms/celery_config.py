from __future__ import absolute_import, unicode_literals

import os
from datetime import timedelta

from celery import Celery

# set the default Django settings module for the 'celery' program.
from celery.task import periodic_task
from django.utils import timezone


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testcms.settings')

app = Celery()  # noqa


# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings', namespace='CELERY')

# There is no need to pass args to autodiscover func in Celery >4.x
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@periodic_task(run_every=timedelta(minutes=1))
def scheduled_time_publication():
    """
    Check every minutes if post have to be published or not
    :return: updated TournamentPosts' object with is_publish=True
    """
    from cms.models import TournamentPost
    TournamentPost.objects.filter(scheduled_time__lte=timezone.now()).update(is_publish=True)
