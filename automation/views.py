from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import GeneratedArticle,ContentInteraction,CourseProgress,FavoriteContent

def articles_list(request):
    articles=GeneratedArticle.objects.filter(approved=True)
    return render(request,"automation/articles.html",{"articles":articles})

@login_required
def like_article(request,id):
    article=get_object_or_404(GeneratedArticle,id=id)
    ContentInteraction.objects.create(user=request.user,content_title=article.title,interaction_type="like")
    return redirect("/articles/")

@login_required
def favorite_article(request,id):
    article=get_object_or_404(GeneratedArticle,id=id)
    FavoriteContent.objects.create(user=request.user,title=article.title)
    return redirect("/articles/")

@login_required
def dashboard(request):
    courses=CourseProgress.objects.filter(user=request.user)
    favorites=FavoriteContent.objects.filter(user=request.user)
    return render(request,"dashboard/dashboard.html",{"courses":courses,"favorites":favorites})
