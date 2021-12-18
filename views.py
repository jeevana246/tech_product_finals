from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

    
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.core.mail import send_mail, BadHeaderError

from compeapp.models import administrator, competition, event, hackathon, scholar



def index(request):
    return render(request,'index.html')

def ureg(request):
    return render(request,'index.html')

def adminlogin(request): 
    if request.method=='POST':
        username = request.POST['username']
        password1 = request.POST['password']
        un_key = request.POST['key']
        if(un_key=="admin123"):
            if administrator.objects.filter(username=username).exists():
                print("hiii")
                obj = administrator.objects.get(username=username)
                field_value = getattr(obj, 'password')
                if(password1==field_value):
                    return render(request,'res.html')
                else:
                    messages.info(request,'Check your password')
                    return redirect('adminlogin')
            else:
                messages.info(request,'invalid credentials')
                return redirect('adminlogin')
        else:
            messages.info(request,'unique key is invalid!!!')
            return render(request,'login.html')
    else:    
        return render(request,'login.html')


def adminregister(request):
    if request.method == 'POST':
        print("hi")
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        print(password1)
        print(password2)
        if password1==password2:
            print("pass")
            if administrator.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                print("username exists")
            elif administrator.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                print("Email exists")
            else:
                user = administrator.objects.create(first_name=first_name,last_name=last_name,email=email,username=username,password=password1)
                user.save()
                messages.info(request,"created successfully for customer role")
                return redirect('adminlogin')
        else:
            messages.info(request,"password does not match")           

    return render(request,'register.html')


def scholarlogin(request): 
    if request.method=='POST':
        username = request.POST['username']
        password1 = request.POST['password']
        if scholar.objects.filter(username=username).exists():
            print("hiii")
            obj = scholar.objects.get(username=username)
            field_value = getattr(obj, 'password')
            if(password1==field_value):
                return render(request,'admin_dashboard.html')
                
            else:
                messages.info(request,'Check your password')
                return redirect('scholarlogin')
        else:
            messages.info(request,'invalid credentials')
            return redirect('scholarlogin')
    else:    
        return render(request,'login1.html')


def scholarregister(request):
    if request.method == 'POST':
        print("hi")
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        print(password1)
        print(password2)
        if password1==password2:
            print("pass")
            if scholar.objects.filter(username=username).exists():
                messages.info(request,'Username already exists')
                print("username exists")
            elif scholar.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                print("Email exists")
            else:
                user = scholar.objects.create(first_name=first_name,last_name=last_name,email=email,username=username,password=password1)
                user.save()
                messages.info(request,"created successfully for customer role")
                return redirect('scholarlogin')
        else:
            messages.info(request,"password does not match")           

    return render(request,'register1.html')

def admin_dashboard(request):
    return render(request,'admin_dashboard.html')

def hackathons(request):
    reslist = list(hackathon.objects.all())
    context = {'reslist':reslist}
    return render(request,'hackathon.html',context)

def competitions(request):
    competitions_list = list(competition.objects.all())
    context = {'competitions_list': competitions_list}
    return render(request,'competition.html',context) 

def events(request):
    e_list = list(event.objects.all())
    context = {'e_list': e_list}
    return render(request,'events.html',context) 

def adminlogout(request):
    return render(request,'index.html') 