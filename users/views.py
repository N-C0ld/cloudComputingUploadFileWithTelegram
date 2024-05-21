from django.shortcuts import render, redirect
from . forms import createUserForm, loginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    form = createUserForm()
    if(request.method == "POST"):
        form = createUserForm(request.POST)
        if(form.is_valid()):
            form.save()

            return redirect("/login")
    context={'registerform': form}
    return render(request, 'userRegister.html', context=context)

def login(request):
    form = loginForm()
    if(request.method == "POST"):
        form = loginForm(request, data=request.POST)

        if(form.is_valid()):
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if(user is not None):
                auth.login(request, user)
                return redirect("/dashboard")
            
    context = {"loginform": form}
    return render(request, 'login.html', context=context)

@login_required(login_url="/login")
def dashboard(request):
    return render(request, "dashboard.html")

def userLogOut(request):
    auth.logout(request)
    return redirect("/login")