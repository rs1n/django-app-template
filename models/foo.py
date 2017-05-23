from django.db import models
from django.utils.translation import ugettext_lazy as _

from . import timestampable


class Foo(timestampable.Timestampable):
    'A sample model.'

    name = models.CharField(max_length=255, verbose_name=_('name'))
    description = models.TextField(
        blank=True, default='', verbose_name=_('description'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('foo')
        verbose_name_plural = _('foos')
