from django.views.generic import TemplateView
from core.models import Employee


class EmployeeListView(TemplateView):
    template_name = "core/employee_table.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['emp_name'] = Employee.objects.first()
        return context
