from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from courses.models import Course
from articles.models import Article

def home(request):
    courses=Course.objects.all()
    articles=Article.objects.all()
    return render(request,"home.html",{"courses":courses,"articles":articles})

def courses(request):
    courses=Course.objects.all()
    return render(request,"courses.html",{"courses":courses})

def articles(request):
    articles=Article.objects.all()
    return render(request,"articles.html",{"articles":articles})

def user_login(request):

    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(request,username=username,password=password)

        if user is not None and not user.is_staff:
            login(request,user)
            return redirect("/dashboard/")

    return render(request,"auth/login.html")

def register(request):

    if request.method=="POST":

        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username,email=email,password=password)
            return redirect("/user-login/")

    return render(request,"auth/register.html")

def admin_login(request):

    if request.method=="POST":

        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(request,username=username,password=password)

        if user is not None and user.is_staff:
            login(request,user)
            return redirect("/admin-dashboard/")

    return render(request,"dashboard/admin_login.html")

@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect("/")
    return render(request,"dashboard/admin_dashboard.html")

@login_required
def dashboard(request):

    dummy_courses=[
    {"title":"Docker Mastery"},
    {"title":"Kubernetes Basics"},
    {"title":"CI/CD Pipeline"},
    {"title":"Terraform Intro"}
    ]

    dummy_articles=[
    {"title":"DevOps Roadmap"},
    {"title":"Linux for DevOps"},
    {"title":"Monitoring Guide"},
    {"title":"Cloud Architecture"}
    ]

    return render(request,"dashboard/dashboard.html",{
    "courses":dummy_courses,
    "articles":dummy_articles
    })
