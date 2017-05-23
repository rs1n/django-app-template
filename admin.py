{{ unicode_literals }}from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.Foo)
class FooAdmin(admin.ModelAdmin):
    pass


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    pass
