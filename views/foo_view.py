from django import shortcuts

from . import {{ app_name }}_view


class FooList({{ app_name }}_view.{{ camel_case_app_name }}View):
    'A sample view.'

    def get(self, request):
        return shortcuts.render(request, '{{ app_name }}/foo/index.html')
