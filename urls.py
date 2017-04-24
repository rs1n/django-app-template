from django.conf import urls

from .views import foo_view


# Define the app namespace and routes.
app_name = '{{ app_name }}'
urlpatterns = [
    urls.url(r'^$', foo_view.FooList.as_view(), name='foo_list'),
]
