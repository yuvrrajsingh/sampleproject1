from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from . models import *
# Create your views here.

def error_404_view(request, exception):

    return render(request,'login/404.html')


def index(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')

    elif request.method == 'POST':
        l = Login()
        username = request.POST['user']
        password = request.POST['pass']

        s = SignUp.objects.all()
        mydict = {
            'remember' : False
        }
        for i in s:
            if username == i.username:
                mydict['remember'] = True
                break

        if mydict['remember'] == True:
            mydict['signup_data'] = s
            return redirect('allapps')
            # return render(request, 'login/register.html', context=mydict)
        else:
            return redirect('signup')

        # return render(request, 'login/register.html', context=mydict)

def submitform(request):
    # l = Login()
    # l.username = request.GET['user']
    # l.password = request.GET['pass']
    pass

def signup(request):
    if request.method == 'GET':
        return render(request, 'login/signup.html')

    elif request.method == 'POST':
        s = SignUp()
        s.name = request.POST['name']
        s.username = request.POST['username']
        s.email = request.POST['email']
        s.password = request.POST['password']
        s.confirm = request.POST['confirm']

        if s.password == s.confirm:
            s.save()

            return redirect('/')
            # return render(request, 'login/login.html')
        else:
            mydict = {
                'error' : True
            }
            return render(request, 'login/signup.html', context=mydict)

def register(request):
    return render(request, 'login/forgot.html')

def allapps(request):
    return render(request, 'login/allapps.html')

