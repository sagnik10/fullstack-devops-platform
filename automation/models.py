from django.db import models
from django.contrib.auth.models import User


class GeneratedArticle(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="articles", blank=True, null=True)
    approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


class ContentInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_title = models.CharField(max_length=255, default="")
    interaction_type = models.CharField(max_length=50, default="")
    created = models.DateTimeField(auto_now_add=True)


class CourseProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=255, default="")
    progress = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)


class FavoriteContent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default="")
    created = models.DateTimeField(auto_now_add=True)