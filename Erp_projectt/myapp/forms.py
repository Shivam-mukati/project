from django import forms
from .models import Department, Designation, Employee


class dep_addform(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class des_addform(forms.ModelForm):
    class Meta:
        model = Designation
        fields = '__all__'
        
class emp_addform(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        