import json

from django.conf import settings
from django.db import models
from channels import Group
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class InfoDate(models.Model):
    """
    Abstract class about date:
        creation_date: automatically added date when object was created
        update_date: automatically added date when object was updated(changed etc)
    """
    creation_date = models.DateTimeField(_('creation_date'), auto_now_add=True)
    update_date = models.DateTimeField(_('update_date'), auto_now=True)

    class Meta:
        abstract = True


class Room(InfoDate):
    """
    A Room model for people to chat in.
    title: CharField, show the name for the room
    staff_only: BooleanField,  If only "staff" users are allowed (is_staff on django's User)
    """

    # Room title
    title = models.CharField(_('title'), max_length=255)

    # If only "staff" users are allowed (is_staff on django's User)
    staff_only = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('room')
        verbose_name_plural = _('rooms')


class Message(InfoDate):
    """
    Model of message for chat
    text: TextField, message body
    room: ForeignKey, connect to Room
    sender: ForeignKey, Add author of message
    """
    text = models.TextField(_('text_message'))
    room = models.ForeignKey('Room', on_delete=models.CASCADE, related_name=_('room_messages'))
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name=_('sender_message'))

    class Meta:
        verbose_name = _('message')
        verbose_name_plural = _('messages')
        ordering = ('creation_date', )
