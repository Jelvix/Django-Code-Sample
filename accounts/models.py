from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager

from django.utils.translation import ugettext_lazy as _


# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    """
    User model
    email: EmailField, email field
    first_name: CharField, get a first users' name
    last_name: CharField, get a last users' name
    date_added: DateTimeField, date when user had registered
    is_active: BooleanField, show if this user still exist
    avatar: ImageField, user avatar
    is_staff: BooleanField, show if user is admin
    """
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_added = models.DateTimeField(_('date added'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    avatar = models.ImageField(_('avatar'), upload_to='avatars/', null=True, blank=True)
    is_staff = models.BooleanField(_('admin'), default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    def __str__(self):
        """
        Create name for every Users' object
        :return: name in str
        """
        if not self.last_name:
            if not self.first_name:
                return self.email
            return self.get_short_name()
        return self.get_full_name()

    def save(self, *args, **kwargs):
        if not User.objects.filter(is_superuser=True).exists():
            self.is_superuser = True
            super(User, self).save(*args, **kwargs)
        else:
            super(User, self).save(*args, **kwargs)
