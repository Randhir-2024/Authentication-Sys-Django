from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    return render(request, 'HomePage.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        if pass1==pass2:
            my_user = User.objects.create_user(username=uname,email=email,password=pass1)
            my_user.save()
            return redirect('login')
        else:
            return HttpResponse("Password does not match")

    return render(request, 'SignupPage.html')

def login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=uname,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('home')
        else:
            return HttpResponse('Username or Password is Incorrect')
    return render(request, 'LoginPage.html')

def logout(request):
    return redirect('login')