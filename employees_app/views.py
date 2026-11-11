from django.shortcuts import render
from .models import Employee
from django.db.models import Avg, Q
from datetime import date


def employee_overview(request):

    # Hier die entsprechenden Filter anlegen und die context-Variable definieren, um die Daten an das Template zu übergeben
    employees = Employee.objects.all()

    salary_gt_3000 = employees.filter(salary__gt=3000)

    count_salary_gt_5000 = employees.filter(salary__gte=5000).count()

    avg_sales_employees = employees.filter(department__name="Sales").aggregate(
        Avg("salary")
    )["salary__avg"]
    avg_sales_employees = round(avg_sales_employees, 2)

    employees_before_date = employees.filter(hire_date__lt=date(2022, 1, 1)).exclude(
        department__name="HR"
    )

    context = {
        "all": employees,
        "salary_gt_3000": salary_gt_3000,
        "count_salary_gt_5000": count_salary_gt_5000,
        "avg_sales": avg_sales_employees,
        "employees_before_date": employees_before_date,
    }
    return render(request, "employee_list.html", context)
