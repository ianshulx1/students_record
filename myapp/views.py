import re
from turtle import home
from django.shortcuts import redirect, render,HttpResponseRedirect
from .forms import Student_data_form
from .models import Student_data
from django.views import View
from django.contrib.auth import authenticate, login, logout
from . tokens import generate_token
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages




class HomeView(View):

 def get(self, request):
  form = Student_data_form()
  candidates = Student_data.objects.all()
  return render(request, 'myapp/add_data.html', { 'candidates':candidates, 'form':form})

 def post(self, request):
  form = Student_data_form(request.POST, request.FILES)
  if form.is_valid():
   form.save()
   return HttpResponseRedirect('list')

   
@login_required
def application_form(request, pk):
  candidate = Student_data.objects.get(pk=pk)
  return render(request, 'myapp/candidate.html', {'candidate':candidate})







@login_required
def stu_list(request):
   student=Student_data.objects.all()
   return render(request, 'myapp/list.html', {'student': student})

# delete

@login_required
def delete_data(request, id):
   if request.method == 'POST':
      pi = Student_data.objects.get(pk=id)
      pi.delete()
      return redirect(stu_list)

@login_required
def update_data(request, id):
   if request.method == 'POST':
      pi=Student_data.objects.get(pk=id)
      form = Student_data_form(request.POST, request.FILES, instance=pi)
      if form.is_valid():
         form.save

   else:
      pi=Student_data.objects.get(pk=id)
      form = Student_data_form(instance=pi)
   return render(request, "myapp/updatedata.html", {'form': form})



def menu(request):
    return render(request, 'myapp/home.html')



#Authentication 

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        
        
        
        
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signup')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('signup')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('signup')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('signup')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        
        
        
        
        myuser.is_active = False
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!! please admins to activate your account")

        
        return redirect(signin)
        
        
    return render(request, "myapp/signup.html")





def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            
            return redirect(menu)
        else:
            messages.error(request, "Bad Credentials!! Please check username or password ")
            return redirect(signin)
    
    return render(request, "myapp/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('signin')

   

