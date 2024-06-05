from django.core.management.base import BaseCommand
from core.models import Employee, Department


class Command(BaseCommand):
    help = 'Stores employee and department data from image'

    def handle(self, *args, **options):
        departments = {
            '00': {'dep_name': 'Executive', 'location': 'Silom'},
            '10': {'dep_name': 'Accounting', 'location': 'Silom'},
            '20': {'dep_name': 'Administration', 'location': 'Sukhumvit'},
            '30': {'dep_name': 'Sales', 'location': 'Ratchada'},
            '40': {'dep_name': 'Marketing', 'location': 'Silom'},
            '50': {'dep_name': 'Research', 'location': 'Sukhumvit'},
        }

        for dep_no, dep_data in departments.items():
            department, created = Department.objects.get_or_create(
                dep_no=dep_no,
                defaults={
                    'dep_name': dep_data['dep_name'],
                    'location': dep_data['location']
                }
            )

        employees = [
            {'emp_num': '0001', 'emp_name': 'Kanjana', 'hire_date': '1994-10-07', 'salary': 50000.00, 'position': 'Managing Director', 'dep_no': '00', 'head_no': None},
            {'emp_num': '1001', 'emp_name': 'Surasit', 'hire_date': '1994-03-15', 'salary': 30000.00, 'position': 'Manager', 'dep_no': '10', 'head_no': '0001'},
            {'emp_num': '1002', 'emp_name': 'Jintana', 'hire_date': '1993-10-31', 'salary': 20000.00, 'position': 'Supervisor', 'dep_no': '10', 'head_no': '1001'},
            {'emp_num': '1003', 'emp_name': 'Siriwan', 'hire_date': '1993-06-13', 'salary': 9000.00, 'position': 'Clerk', 'dep_no': '10', 'head_no': '1001'},
            {'emp_num': '2001', 'emp_name': 'Ternjai', 'hire_date': '1994-11-01', 'salary': 24000.00, 'position': 'Manager', 'dep_no': '20', 'head_no': '0001'},
            {'emp_num': '2002', 'emp_name': 'Chai', 'hire_date': '1993-05-14', 'salary': 14000.00, 'position': 'Clerk', 'dep_no': '20', 'head_no': '2001'},
            {'emp_num': '3001', 'emp_name': 'Benjawan', 'hire_date': '1994-06-11', 'salary': 29000.00, 'position': 'Manager', 'dep_no': '30', 'head_no': '0001'},
            {'emp_num': '3002', 'emp_name': 'Tanachole', 'hire_date': '1994-06-14', 'salary': 25000.00, 'position': 'Supervisor', 'dep_no': '30', 'head_no': '3001'},
            {'emp_num': '3003', 'emp_name': 'Arlee', 'hire_date': '1993-08-15', 'salary': 17000.00, 'position': 'Salesman', 'dep_no': '30', 'head_no': '3001'},
            {'emp_num': '3004', 'emp_name': 'Mitree', 'hire_date': '1993-12-05', 'salary': 13000.00, 'position': 'Salesman', 'dep_no': '30', 'head_no': '3001'},
            {'emp_num': '3005', 'emp_name': 'Tawatchai', 'hire_date': '1994-07-03', 'salary': 10000.00, 'position': 'Salesman', 'dep_no': '30', 'head_no': '3001'},
            {'emp_num': '4001', 'emp_name': 'Wichai', 'hire_date': '1993-12-26', 'salary': 33000.00, 'position': 'Manager', 'dep_no': '40', 'head_no': '0001'},
            {'emp_num': '4002', 'emp_name': 'Thidarat', 'hire_date': '1994-12-01', 'salary': 9000.00, 'position': 'Clerk', 'dep_no': '40', 'head_no': '4001'}
        ]

        for emp_data in employees:
            department = Department.objects.get(dep_no=emp_data['dep_no'])
            employee = Employee(
                emp_num=emp_data['emp_num'],
                emp_name=emp_data['emp_name'],
                hire_date=emp_data['hire_date'],
                salary=emp_data['salary'],
                position=emp_data['position'],
                dep_no=department,
                head_no=emp_data['head_no']
            )
            employee.save()

        self.stdout.write(self.style.SUCCESS('Employee and department data stored successfully!'))