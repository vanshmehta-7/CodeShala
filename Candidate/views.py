from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from Client.models import Emp, Organization, Designation, Parent, Child
from datetime import datetime
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.http import HttpResponseRedirect

# Create your views here.
def emp_create(request):
    context = {}
    context['organizations'] = Organization.objects.all()
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['pass2']
        organization_val = request.POST['organization']
        organization = Organization.objects.all().filter(name=organization_val)[0]
        dob = request.POST['dob']
        if password != password2:
            context['message'] = "Your Passwords Don't Match. Try Again."
        else:
            if username == '' or email == '' or password == '':
                context['message'] = "Fields aren't filled properly. Please Try again"
            elif len(list(User.objects.all().filter(username=username))) > 0 or len(list(User.objects.all().filter(email=email))) > 0 :
                context['message'] = "Organization with that username already exists."
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                if user is not None:
                    login(request, user)
                else:
                    context['message'] = "We could not sign you up."
                employee = Emp.objects.create(name=user.username, user=user, points=0, organization=organization,dob=datetime.strptime(dob , '%Y-%m-%dT%H:%M'))
    return render(request, 'candidate/emp_create.html', context)

def emp_design(request):
    user = request.user
    context = {}
    context['valid'] = True
    if user.is_active:
        employee = Emp.objects.get(user=user)
        org = employee.organization
        context['designations'] = org.designation_set.all()
        if request.method == "POST":
            design = request.POST['designation']
            print(design)
            employee.designation = design
            employee.save()
    else:
        context['valid'] = False
    return render(request, 'candidate/emp_design.html', context)

def emp_login(request):
    user = request.user
    context = {}
    context['valid1'] = True
    if not user.is_active:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            print(user)
            if user is not None:
                auth.login(request, user)
            else:
                context['message'] = "Please check you Username / Password and Try Again"
    else:
        context['valid1'] = False
    return render(request, 'candidate/emp_login.html', context)

def emp_child_list(request):
    context = {}
    user = request.user
    context['valid'] = True
    if user.is_active:
        employee = Emp.objects.get(user=user)
        child_em = []
        try:
            parent = Parent.objects.get(emp=employee)
            children = list(parent.child_set.all())
            for child in children:
                child_em.append(child.emp)
        except:
            pass
        design_text = employee.designation
        org = employee.organization
        design_instance = Designation.objects.get(designation=design_text, organization=org)
        priority = design_instance.priority
        under = Designation.objects.all().filter(priority__gt=priority, organization=org) 
        print(under)
        employees = []
        for design in under:
            for e in list(Emp.objects.all().filter(designation=design.designation)):
                if e not in child_em:
                    employees.append(e)
        con_emp = []
        if request.method == "POST":
            term = request.POST['filter']
            for emp in employees:
                if term.lower() in emp.name.lower() or term.lower() in emp.user.email.lower():
                    con_emp.append(emp)
        else:
            con_emp = employees
        context['employees'] = con_emp
    else:
        context['valid'] = False
    return render(request, 'candidate/emp_setchild.html', context)

def emp_setchild(request, pk):
    user = request.user
    emp = Emp.objects.get(user=user)
    if user.is_active:
        selected = User.objects.get(id=pk)
        selected_emp = Emp.objects.get(user=selected)
        parent_inst, created = Parent.objects.get_or_create(emp=emp)
        child, ucreated = Child.objects.get_or_create(emp=selected_emp)
        child.parent.add(parent_inst)
        return HttpResponseRedirect(reverse('emp_child_list'))
    return render(request, 'candidate/emp_setchild.html')
