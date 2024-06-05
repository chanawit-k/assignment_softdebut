from django.urls import path
from . import views

app_name = 'core'


urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='emp_list'),
    path('create', views.EmployeeCreateView.as_view(), name='emp_create'),
]
