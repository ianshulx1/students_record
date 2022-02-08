from django import forms
from .models import Student_data


GENDER_CHOICES = [
 ('Male', 'Male'),
 ('Female', 'Female')
]

CATEGORY = [
 ('SC', 'SC'),
 ('ST', 'ST'),
 ('OBC', 'OBC'),
 ('GENERAL', 'GENERAL'),
 ('OTHERS', 'OTHERS'),

]

class Student_data_form(forms.ModelForm):
 gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
 category = forms.ChoiceField(label='Category', choices=CATEGORY, widget=forms.RadioSelect)
 class Meta:
  model = Student_data
  fields = ['first_name', 'middle_name', 'last_name', 'fathers_name', 'fathers_occupation', 'mothers_name','mothers_occupation', 'dob', 'gender', 'category','address', 'city', 'pin','mobile', 'mobile2', 'email',  'course', 'department', 'mark10', 'mark10_obtained' , 'mark10_total', 'mark12',  'mark12_obtained' , 'mark12_total', 'mark_graduation', 'mark_graduation_obtained' , 'mark_graduation_total' , 'photo', 'sign', 'Adhaar', 'Adhaar_no' ,'pan', 'pan_no', 'caste', 'income', 'address_certificate' ,'charactor_certificate']
  labels = {'first_name':'First Name', 'middle_name':'Middle Name', 'last_name':'Last Name' ,'fathers_name': 'Fathers Name' ,'fathers_occupation': 'Fathers occupation' , 'mothers_occupation': 'Mothers occupation' , 'dob': 'Date of Birth', 'pin':'Pin Code', 'mobile':'Mobile No.', 'mobile2':'Fathers mobile no.', 'email':'Email ID', 'photo':'Students Image', 'Adhaar':'Adhaar Card', 'pan':'Pan Card', 'caste':'Caste Certificate', 'income':'Income Certificate', 'charactor_certificate': 'Charactor Certificate', 'mark10': '10th Marksheet', 'mark12': '12th Marksheet', 'mark10_obtained':'Obtained marks in 10th', 'mark10_total':'Total marks in 10th','mark12_obtained':'Obtained marks in 12th' , 'mark12_total':'Total marks in 12th', 'mark_graduation_obtained':'Obtained marks in graduation' , 'mark_graduation_total':'Total marks in graduation', 'mark_graduation':'Graduation degree (Only MBA students)', 'address_certificate':'Address Certificate'}
  
  
  widgets = {
   'first_name':forms.TextInput(attrs={'class':'form-control'}),
   'middle_name':forms.TextInput(attrs={'class':'form-control'}),
   'last_name':forms.TextInput(attrs={'class':'form-control'}),

   'fathers_name':forms.TextInput(attrs={'class':'form-control'}),
   'fathers_occuption':forms.TextInput(attrs={'class':'d-inline'}),

   
   'mothers_name':forms.TextInput(attrs={'class':'form-control'}),
   'mothers_occuption':forms.TextInput(attrs={'class':'d-inline'}),

   'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
   'category':forms.TextInput(attrs={'class':'form-control'}),

   'address':forms.TextInput(attrs={'class':'form-control'}),
   'city':forms.TextInput(attrs={'class':'form-control'}),
   
   'pin':forms.NumberInput(attrs={'class':'form-control'}),
   'state':forms.Select(attrs={'class':'form-select'}),
   'mobile':forms.NumberInput(attrs={'class':'form-control'}),
   'mobile2':forms.NumberInput(attrs={'class':'form-control'}),
   'email':forms.EmailInput(attrs={'class':'form-control'}),


   'photo':forms.FileInput(attrs={'class':'form-control'}),
   'Adhaar':forms.FileInput(attrs={'class':'form-control'}),
   'Adhaar_no':forms.NumberInput(attrs={'class':'form-control'}),
   'pan':forms.FileInput(attrs={'class':'form-control'}),
   'pan_no':forms.TextInput(attrs={'class':'form-control'}),
   'caste':forms.FileInput(attrs={'class':'form-control'}),
   'income':forms.FileInput(attrs={'class':'form-control'}),
   'address_certificate':forms.FileInput(attrs={'class':'form-control'}),
   'charactor_certificate':forms.FileInput(attrs={'class':'form-control'}),


   'mark10':forms.FileInput(attrs={'class':'form-control', 'placeholder':'Upload 10th marksheet'}),
   'mark10_obtained':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Obtained Marks in 10th' }),
   'mark10_total':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Total Marks in 10th'}),

   'mark12':forms.FileInput(attrs={'class':'form-control'}),
   'mark12_obtained':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Obtained Marks in 12th' }),
   'mark12_total':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Total Marks in 12th'}),
   
   'mark_graduation':forms.FileInput(attrs={'class':'form-control'}),
   'mark_graduation_obtained':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Obtained Marks in Graduation' }),
   'mark_graduation_total':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Total Marks in Graduation'}),
   
   'sign':forms.FileInput(attrs={'class':'form-control'}),
  }

