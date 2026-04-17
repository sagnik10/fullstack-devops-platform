from django.urls import path
from . import views

urlpatterns=[
path("",views.courses,name="courses"),
path("docker/",views.docker,name="docker"),
path("kubernetes/",views.kubernetes,name="kubernetes"),
path("terraform/",views.terraform,name="terraform"),
path("cicd/",views.cicd,name="cicd"),
]