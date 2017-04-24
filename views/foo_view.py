from . import {{ app_name }}_view


# A sample view.
class FooList({{ app_name }}_view.{{ camel_case_app_name }}View):
    template_name = '{{ app_name }}/foo/index.html'
