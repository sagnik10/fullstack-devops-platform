from django.urls import path
from . import views

urlpatterns = [

    path("", views.home, name="home"),

    path("courses/", views.courses, name="courses"),

    path("articles/", views.articles, name="articles"),

    path("dashboard/", views.dashboard, name="dashboard"),

    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),

    path("admin-login/", views.admin_login, name="admin_login"),

]
