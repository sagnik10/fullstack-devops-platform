from django.urls import path
from . import views

urlpatterns = [

path("",views.article_list,name="articles"),

path("devops-roadmap/",views.devops_roadmap,name="devops_roadmap"),

path("docker-guide/",views.docker_guide,name="docker_guide"),

path("kubernetes-basics/",views.kubernetes_basics,name="kubernetes_basics"),

path("cicd-pipelines/",views.cicd_pipelines,name="cicd_pipelines"),

]