from django.shortcuts import render,  redirect, get_object_or_404
from.forms import  *
from . models import Department,Designation,Employee

# Create your views here.

def show_department(request):
    if request.method == 'POST':
        dp_name= request.POST['dp_name']
        if dp_name:
            dp = Department.objects.filter(dp_name__icontains=dp_name)
            return render(request, 'show_dp.html', {'dp': dp})
    dp=Department.objects.all()
    return render(request, 'show_dp.html', {'dp': dp})


def show_designation(request):
    ds=Designation.objects.all()
    return render(request, 'show_ds.html', {'ds': ds})


def show_employee(request):
    emp=Employee.objects.all()
    return render(request, 'show_emp.html', {'emp': emp})






def department_add(request):
    if request.method=='POST':
        myform=dep_addform(data=request.POST)  
        #request.POST['name']
        if myform.is_valid():
            myform.save()
            return redirect('show_dp')
        return redirect('add_dp')
    else:
        myform=dep_addform()
        return render(request, 'add_dp.html', {'myform': myform})
    
def update_department(request,pk):
    dp=get_object_or_404(Department,pk=pk)
    
    if request.method=='POST':
        myform=dep_addform(instance=dp,data=request.POST)
        if myform.is_valid():
            myform.save()
            return redirect('show_dp')
        else:
            return redirect('add_dp')

    myform=dep_addform(instance=dp)
    return render(request, 'upd.html', {'myform': myform})


def delete_department(request, pk):
    dp=get_object_or_404(Department,pk=pk)
    dp.delete()
    return redirect('show_dp')






def designation_add(request):
    if request.method=='POST':
        myform=des_addform(data=request.POST)  
        #request.POST['name']
        if myform.is_valid():
            myform.save()
            return redirect('show_ds')
        return redirect('add_ds')
    else:
        myform=des_addform()
        return render(request, 'add_ds.html', {'myform': myform})



def update_designation(request, pk):    
    ds=get_object_or_404(Designation,pk=pk)
    
    if request.method=='POST':
        myform=des_addform(instance=ds,data=request.POST)
        if myform.is_valid():
            myform.save()
            return redirect('show_ds')
        else:
            return redirect('add_ds')

    myform=des_addform(instance=ds)
    return render(request, 'upd.html', {'myform': myform})


def delete_designation(request, pk):
    ds=get_object_or_404(Designation,pk=pk)
    ds.delete()
    return redirect('show_ds')





def employee_add(request):
    if request.method=='POST':
        myform=emp_addform(data=request.POST)  
        #request.POST['name']
        if myform.is_valid():
            myform.save()
            return redirect('show_emp')
        return redirect('add_emp')
    else:
        myform=emp_addform()
        return render(request, 'add_emp.html', {'myform': myform})
    

def update_employee(request, pk):
    emp=get_object_or_404(Employee,pk=pk)
    
    if request.method=='POST':
        myform=emp_addform(instance=emp,data=request.POST)
        if myform.is_valid():
            myform.save()
            return redirect('show_emp')
        else:
            return redirect('add_emp')

    myform=emp_addform(instance=emp)
    return render(request, 'upd.html', {'myform': myform})


def delete_employee(request, pk):
    emp=get_object_or_404(Employee,pk=pk)
    emp.delete()
    return redirect('show_emp')




# -------------------sign in and sign up-------------------
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout,authenticate
from django.http import HttpResponse as httpResponse, HttpResponseRedirect
from django.shortcuts import redirect


# Create your views here.
def home(request):
    return render(request, 'home.html')

def sign_up(request):
    if request.method == 'POST':
        myform = UserCreationForm(request.POST)
        if myform.is_valid():
            myform.save()
            msg= "User created successfully"
            return render(request, 'home.html', {'msg': msg})
        else:
            msg = "User creation failed"
            return render(request, 'register.html', {'myform': myform, 'msg': msg})

    else:    
     myform = UserCreationForm()
     return render(request, 'register.html', {'myform': myform})

def sign_in(request):
    if request.method == 'POST':
        myform = AuthenticationForm(request, data=request.POST)
        if myform.is_valid():
            
         u_name = myform.cleaned_data['username']
         u_pass = myform.cleaned_data['password']
         user= authenticate(username=u_name, password=u_pass)
         if user:
              login(request, user)
              request.session ['u_name'] = u_name
              return redirect('hm')
         else:
               return redirect('login_as')
        else:
           return redirect('login_as')
    else:    
     myform = AuthenticationForm()
     return render(request, 'login.html', {'myform': myform})

def logout_as(request):
    logout(request)
    return redirect('login_as')