"""
URL configuration for Erp_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dep_add/',views.department_add,name='add_dp'),
    path('show_dp/',views.show_department,name='show_dp'),
    path('update_dp/<str:pk>/', views.update_department, name='upd_dp'),
    path('delete_dp/<str:pk>/', views.delete_department, name='del_dp'),
    #designtion urls
    path('des_add/',views.designation_add,name='add_ds'),
    path('show_ds/',views.show_designation,name='show_ds'),
    path('update_ds/<str:pk>/', views.update_designation, name='upd_ds'),
    path('delete_ds/<str:pk>/', views.delete_designation, name='del_ds'),
    #employee urls
    path('emp_add/',views.employee_add,name='add_emp'),
    path('show_emp/',views.show_employee,name='show_emp'),
    path('update_emp/<str:pk>/', views.update_employee, name='upd_emp'),
    path('delete_emp/<str:pk>/', views.delete_employee, name='del_emp'),
    # user urls
        path('', views.home, name='hm'),
    path('sign_in/', views.sign_in, name='login_as'),
    path('sign_up/', views.sign_up, name='register_as'),
    path('logout/', views.logout_as, name='lg'),
    
]