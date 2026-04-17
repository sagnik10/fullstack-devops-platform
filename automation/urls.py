from django.urls import path
from . import views

urlpatterns=[
path("",views.dashboard,name="dashboard"),
path("articles/",views.articles_list,name="articles"),
path("like/<int:id>/",views.like_article,name="like_article"),
path("favorite/<int:id>/",views.favorite_article,name="favorite_article")
]