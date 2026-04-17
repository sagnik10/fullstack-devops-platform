from django.shortcuts import render

def courses(request):
    return render(request,"courses.html")

def docker(request):
    return render(request,"courses/docker.html")

def kubernetes(request):
    return render(request,"courses/kubernetes.html")

def terraform(request):
    return render(request,"courses/terraform.html")

def cicd(request):
    return render(request,"courses/cicd.html")