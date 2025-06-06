from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Department(models.Model):
    dp_id = models.CharField(max_length=30,primary_key=True)
    dp_name = models.CharField(max_length=30)
    desciptions = models.CharField(null=True,blank=True,max_length=100)
    def __str__(self):
        return self.dp_name

class Designation(models.Model):
    ds_id = models.CharField(primary_key=True, max_length=10)
    ds_name = models.CharField(max_length=30)
    desciptions = models.CharField(null=True,blank=True,max_length=100)
    def __str__(self):
        return self.ds_name
    
class Employee(models.Model):
    emp_id = models.CharField(primary_key=True, max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    mother_name = models.CharField(max_length=30)
    emp_age = models.IntegerField()
    emp_contact = models.CharField(max_length=13)
    salary = models.IntegerField()
    emp_address = models.TextField(max_length=100)
    join_date = models.DateField(null=True,blank=True)

    
    # Foreign Key Relationships
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)
    # emp_profile = models.FileField(upload_to='emp_profile',null=True,blank=True)
    
    def __str__(self):
        return f'{self.first_name}{self.last_name} {self.join_date}'
