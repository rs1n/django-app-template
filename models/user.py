from django.contrib.auth import models as authmodels
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(authmodels.AbstractUser):
    'User provides a custom user model.'

    phone = models.CharField(
        max_length=100, blank=True, default='', verbose_name=_('phone'))
