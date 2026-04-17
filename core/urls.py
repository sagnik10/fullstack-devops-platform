from django.urls import path
from . import views

urlpatterns=[

path("",views.home),
path("courses/",views.courses),
path("articles/",views.articles),

path("user-login/",views.user_login),
path("register/",views.register),

path("dashboard/",views.dashboard),

path("admin-login/",views.admin_login),
path("admin-dashboard/",views.admin_dashboard),

]
