from django.shortcuts import render, HttpResponse
from .models import Employee, Department, Position
from datetime import datetime
from django.db.models import Q


def index(request):
    return render(request, "index.html")


def view_emp(request):
    emp = Employee.objects.all()
    context = {
        'emps': emp
    }

    print(context)

    return render(request, "view_emp.html", context)


def add_emp(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        department = int(request.POST['department'])
        position = int(request.POST['position'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        email = request.POST['email']


        new_emp = Employee(first_name = first_name, last_name = last_name, department_id= department,position_id= position,salary = salary,bonus =bonus,email= email,hire_date =datetime.now())
        new_emp.save()

        return HttpResponse("Employee added Successfully")

    elif request.method == "GET":
        return render(request, "add_emp.html")

    else:
        return HttpResponse("Add Employee Failed")




def remove_emp(request, emp_id = 0):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }


    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }

    return render(request, "remove_emp.html")


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['department']
        role = request.POST['position']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(department__name__icontains = dept)
        if role:
            emps = emps.filter(position__name__icontains = role)

        context = {
            'emps': emps
        }
        return render(request, 'view_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')