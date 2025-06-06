from django.contrib import admin
from .models import Department,Designation,Employee
from django.utils.html import format_html

# Register your models here.
class Designation_Admin(admin.ModelAdmin):
    list_display = ['ds_id','ds_name','desciptions']
    search_fields = ['ds_id','ds_name']
    list_filter = ['ds_name']
    list_editable = ['desciptions']
    list_per_page = 2
    list_display_links = ['ds_name']
    
admin.site.register(Designation, Designation_Admin)

class Department_Admin(admin.ModelAdmin):
    list_display = ['dp_id','dp_name','desciptions']
    search_fields = ['dp_id','dp_name']
    list_filter = ['dp_name']
    list_editable = ['desciptions']
    list_per_page = 2
    list_display_links = ['dp_name']
admin.site.register(Department, Department_Admin)


class Employee_Admin(admin.ModelAdmin):
    list_display = ['emp_id','first_name','last_name','father_name','mother_name','emp_age','emp_contact','salary','emp_address','department','designation',]
    search_fields = ['emp_id','first_name']
    list_filter = ['emp_age']
    list_editable = ['salary']
    list_per_page = 2
    list_display_links = ['first_name']
    
admin.site.register(Employee, Employee_Admin)
admin.site.index_title = format_html('<span style="color:red; font-weight:bold;">welcome to EIMS</span>')