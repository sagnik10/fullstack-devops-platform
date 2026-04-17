from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def courses(request):
    return render(request,"courses.html")

def articles(request):
    return render(request,"articles.html")

def dashboard(request):
    return render(request,"dashboard/dashboard.html")

def admin_dashboard(request):
    return render(request,"dashboard/admin_dashboard.html")

def admin_login(request):
    return render(request,"dashboard/admin_login.html")
