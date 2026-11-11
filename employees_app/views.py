from django.shortcuts import render
from .models import Employee
from django.db.models import Avg, Q
from datetime import date


def employee_overview(request):

    # Hier die entsprechenden Filter anlegen und die context-Variable definieren, um die Daten an das Template zu übergeben
    all_employees = Employee.objects.all()
    salary_gt_3000 = Employee.objects.filter(salary__gt=3000)
    count_salary_gt_5000 = Employee.objects.filter(salary__gte=5000).count()

    context = {
        "all": all_employees,
        "salary_gt_3000": salary_gt_3000,
        "count_salary_gt_5000": count_salary_gt_5000,
    }
    return render(request, "employee_list.html", context)
