from django.db import models

from . import timestampable


# A sample model.
class Foo(timestampable.Timestampable):
    name = models.CharField(max_length=511)

    def __str__(self):
        return self.name
