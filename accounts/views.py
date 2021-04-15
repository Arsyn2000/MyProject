from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return render(request, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username=username, password=password1,
                                                email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, 'User created')
                return render(request, 'index.html')
        else:
            messages.info(request, 'Password not matching')
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')