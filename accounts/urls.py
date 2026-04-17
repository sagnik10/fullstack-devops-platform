from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("signup/", views.user_signup, name="signup"),
    path("register/", views.user_signup, name="register"),   # ADD THIS
    path("admin-signup/", views.admin_signup, name="admin_signup"),
    path("logout/", views.logout_view, name="logout"),
]