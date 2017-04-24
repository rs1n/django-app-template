{{ unicode_literals }}from django.apps import AppConfig


# Config the application.
class {{ camel_case_app_name }}Config(AppConfig):
    name = '{{ app_name }}'
