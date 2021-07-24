from django.core.checks import messages
from django.forms.widgets import PasswordInput
from django.shortcuts import render
from django.http import HttpResponse, request
from .models import *
from django import forms
from robot import models, forms
from django.shortcuts import redirect
from .models import User
from django.contrib import messages



import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mblog.settings')
django.setup()

#from django import forms


def index(request):
    key = 0
    if 'username' in request.session:
        username = request.session['username']
        key = 1
        message = "登入中"
    return render(request, 'index.html', locals())

def login(request):
    if request.method == 'POST':
        
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
            try:
                user = models.Userdata.objects.get(name = login_name, password = login_password)
                if user.password == login_password:
                    request.session['username'] = user.name
                    request.session['year'] = user.year
                    request.session['month'] = user.month
                    request.session['day'] = user.day
                    request.session['gender'] = user.gender
                    request.session['password'] = user.password
                    
                    return redirect('/')
                else:
                    message = '密碼錯誤'
                    #messages.add_message(request, messages.WARNING, '密碼錯誤')
            except:
                message = '無此帳號'
                #messages.add_message(request, messages.WARNING, '無此帳號')
        else:
            message = '請檢查欄位'
            #messages.add_message(request, messages.INFO, '請檢查欄位')
    else:
        login_form = forms.LoginForm()

    return render(request, 'Login.html', locals())


def logout(request):
    request.session['username'] = None
    key = 0
    return redirect('/')

def signup(request):
    if request.method == 'POST':
        signup_form = forms.SignupForm(request.POST)
        if signup_form.is_valid():
            signup_name = request.POST['username'].strip()
            signup_year = request.POST['year']
            signup_month = request.POST['month']
            signup_day = request.POST['day']
            signup_gender = request.POST['gender']
            
            try:
                user = models.Userdata.objects.get(name = signup_name, year = signup_year, month = signup_month, day = signup_day, gender = signup_gender)
                message = '帳號已存在'
                    #return redirect('/')
            except:
                signup_password = str(signup_year) + str(signup_month) + str(signup_day)
                user = Userdata.objects.create(name = signup_name, year = signup_year, month = signup_month, day = signup_day, gender = signup_gender, password = signup_password)
                user.save()
                message = '帳號已建立成功'
                #messages.add_message(request, messages.WARNING, '無此帳號')
        else:
            message = '請檢查欄位'
            #messages.add_message(request, messages.INFO, '請檢查欄位')
    else:
        signup_form = forms.SignupForm()

    return render(request, 'SignUp.html', locals())

def userinfo(request):
    username = request.session['username']
    useryear = request.session['year']
    usermonth = request.session['month']
    userday = request.session['day']
    usergender = request.session['gender']
    userpassword = request.session['password']
    return render(request, 'userinfo.html', locals())



# Create your views here.




