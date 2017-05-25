import logging

from django import shortcuts

from . import {{ app_name }}_view

logger = logging.getLogger(__name__)


class FooList({{ app_name }}_view.{{ camel_case_app_name }}View):
    'A sample view.'

    def get(self, request):
        logger.info('Foo index page requested')

        return shortcuts.render(request, '{{ app_name }}/foo/index.html')
