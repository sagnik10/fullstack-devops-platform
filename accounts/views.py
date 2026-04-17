from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserSignupForm,AdminSignupForm
from .models import Profile

def user_signup(request):
    if request.method=="POST":
        form=UserSignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            Profile.objects.create(user=user,role="user")
            login(request,user)
            return redirect("/")
    else:
        form=UserSignupForm()
    return render(request,"account/signup.html",{"form":form,"type":"User"})

def admin_signup(request):
    if request.method=="POST":
        form=AdminSignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.is_staff=True
            user.save()
            Profile.objects.create(user=user,role="admin")
            login(request,user)
            return redirect("/dashboard/admin/")
    else:
        form=AdminSignupForm()
    return render(request,"account/signup.html",{"form":form,"type":"Admin"})

def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if user.is_staff:
                return redirect("/dashboard/admin/")
            return redirect("/")
    else:
        form=AuthenticationForm()
    return render(request,"account/login.html",{"form":form})

def logout_view(request):
    logout(request)
    return redirect("/")