from django import forms
from core.models import Employee
from django.core.exceptions import ValidationError


class EmployeeForm(forms.ModelForm):
    emp_num = forms.CharField(error_messages={'required': 'คุณยังไม่ได้กรอกรหัสพนักงาน'})
    emp_name = forms.CharField(error_messages={'required': 'คุณยังไม่ได้กรอกชื่อพนักงาน'})

    class Meta:
        model = Employee
        fields = [
            "emp_num",
            "emp_name",
            "position"
        ]

    def clean_position(self):
        position = self.cleaned_data.get('position')
        if position == 'select':
            raise ValidationError('คุณยังไม่ได้เลือกตำแหน่ง')
        return position
