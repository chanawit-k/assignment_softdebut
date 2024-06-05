from django.views.generic import TemplateView, CreateView
from core.models import Employee
from django.urls import reverse_lazy
from core.forms import EmployeeForm
from django.contrib import messages


class EmployeeListView(TemplateView):
    template_name = "core/employee_table.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['emp_name'] = Employee.objects.first()
        return context


class EmployeeCreateView(CreateView):
    template_name = 'core/employee_form.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('core:emp_list')
