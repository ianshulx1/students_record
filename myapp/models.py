from email.policy import default
from re import T
from django.db import models
import os
COURSE_CHOICE = (
 ('B.tech','B.tech'),
 ('MBA','MBA'),
 ('BCA','BCA'),
 ('BBA','BBA'),
 ('Diploma','Diploma'),
)

DEPARTMENT_CHOICE = (
 ('MBA department','MBA department'),
 ('Computer Science department',' Computer Science department'),
 ('Electrical department','Electrical department'),
 ('Mechanical Department','Mechanical Department'),
 ('Civil Department','Civil Department'),
 ('Electronics and Engineering Department','Electronics and Engineering Department'),
 
)

class Student_data(models.Model):
 first_name = models.CharField(max_length=100)
 middle_name = models.CharField(max_length=100, blank=True)
 last_name = models.CharField(max_length=100)

 
 fathers_name = models.CharField(max_length=100)
 fathers_occupation = models.CharField(max_length=30, blank=True)
 mothers_name = models.CharField(max_length=100)
 mothers_occupation = models.CharField(max_length=30,  blank=True)


 dob = models.DateField(auto_now=False, auto_now_add=False)
 
 gender = models.CharField(max_length=100)
 category = models.CharField(max_length=50)
 address = models.CharField(max_length=180)
 city = models.CharField(max_length=180)
 
 pin = models.PositiveIntegerField()
 course = models.CharField(choices=COURSE_CHOICE, max_length=100)

 mark10_obtained = models.PositiveIntegerField(blank=True)
 mark10_total = models.PositiveIntegerField( blank=True)

 mark12_obtained = models.PositiveIntegerField( blank=True)
 mark12_total = models.PositiveIntegerField(blank=True)
 

 mark_graduation_obtained = models.PositiveIntegerField(blank=True)
 mark_graduation_total = models.PositiveIntegerField(blank=True)

 department = models.CharField(choices=DEPARTMENT_CHOICE, max_length=50, blank=True)

 mobile = models.PositiveIntegerField()
 mobile2 = models.PositiveIntegerField(blank=True)
 email = models.EmailField(blank=True)
 


# DOCUMENTS


 photo = models.ImageField(upload_to='d/1', blank=True, null=True)
 sign = models.ImageField(upload_to='d/8', blank=True, null=True)

 Adhaar = models.FileField(upload_to='d/2', blank=True, null=True)
 Adhaar_no = models.CharField(max_length=12, blank=True)

 pan = models.FileField(upload_to='d/3', blank=True, null=True)
 pan_no = models.CharField(max_length=10,  blank=True)

 caste = models.FileField(upload_to='d/3', blank=True, null=True)
 address_certificate = models.FileField(upload_to='d/3', blank=True, null=True)
 income = models.FileField(upload_to='d/4', blank=True, null=True)
 charactor_certificate = models.FileField(upload_to='d/5', blank=True)
 mark10 = models.FileField(upload_to='d/6', blank=True, null=True)
 mark12 = models.FileField(upload_to='d/7', blank=True, null=True)
 mark_graduation=models.FileField(upload_to='d/8', blank=True, null=True)


    




