from __future__ import unicode_literals

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Like(models.Model):
    """Model for like functionality"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='likes',
                             on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(_('object id'),)
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = _('like')
        verbose_name_plural = _('likes')


