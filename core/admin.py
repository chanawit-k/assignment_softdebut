from django.contrib import admin
from core import models


admin.site.register(models.Employee)
admin.site.register(models.EmployeeBackup)
admin.site.register(models.Department)
