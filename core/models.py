from django.db import models


class Department(models.Model):
    dep_no = models.CharField(max_length=10, primary_key=True)
    dep_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.dep_name


class Employee(models.Model):
    emp_num = models.CharField(max_length=10, primary_key=True)
    emp_name = models.CharField(max_length=255)
    hire_date = models.DateField( null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2,  null=True, blank=True)
    position = models.CharField(max_length=255,  null=True, blank=True)
    dep_no = models.ForeignKey(Department, on_delete=models.CASCADE,  null=True, blank=True)
    head_no = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.emp_name


class EmployeeBackup(models.Model):
    emp_num = models.CharField(max_length=10, primary_key=True)
    emp_name = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    position = models.CharField(max_length=255)

    def __str__(self):
        return self.emp_name
