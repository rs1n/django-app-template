from django.db import models
from django.utils.translation import ugettext_lazy as _

from . import timestampable


# A sample model.
class Foo(timestampable.Timestampable):
    name = models.CharField(max_length=510, default='', verbose_name=_('name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('foo')
        verbose_name_plural = _('foos')
