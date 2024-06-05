from django.views.generic import ListView


class EmployeeListView(ListView):
    template_name = "core/sample_html.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add your context variables here
        context['test_context'] = 'value from views'
        return context