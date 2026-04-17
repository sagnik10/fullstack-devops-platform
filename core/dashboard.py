from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

def admin_login(request):

    if request.method == "POST":

        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)

        if user is not None and user.is_staff:
            login(request,user)
            return redirect('/admin-dashboard/')

    return render(request,"admin_login.html")


@login_required
def admin_dashboard(request):

    if not request.user.is_staff:
        return redirect('/')

    return render(request,"admin_dashboard.html")