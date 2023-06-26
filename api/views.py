from django.shortcuts import render, HttpResponse
from .models import Role, Deperment, Employee
from datetime import datetime
from django.db.models import Q

def index(request):
    return render(request, 'index.html')

def all_api(request):
    emps = Employee.objects.all()
    context = {
        "emps": emps
    }
    print(context)
    return render(request, 'all_api.html', context)

def add_api(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        new_api = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_id=dept, role_id=role, hire_date=datetime.now())
        new_api.save()
        return HttpResponse('Employee added accessfully')
    
    elif request.method == 'GET':
        return render(request, 'add_api.html')
    else:
        return HttpResponse('An exception Occused! Employee not')


def remove_api(request, emp_id = 0):
    if emp_id:
        try:
            remove = Employee.objects.get(id=emp_id)
            remove.delete()
            return HttpResponse("Employee Removed Successfelly")
        except:
            return HttpResponse("Please enter a valid EMP ID")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'remove_api.html', context)

def filter_api(request):
    if request.method == "POST":
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontians = name) | Q(last_name__icontians = name))

        if dept:
            emps = emps.filter(dept__name=dept)
        
        if role:
            emps = emps.filter(role__name = role)

        context = {
            'emps':emps
        }
        return render(request, 'all_api.html', context)
    elif request.method == 'GET':
        return render(request, 'filter_api.html')