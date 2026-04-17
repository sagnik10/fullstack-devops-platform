from django.contrib import admin
from .models import GeneratedArticle, ContentInteraction, CourseProgress, FavoriteContent

admin.site.register(GeneratedArticle)
admin.site.register(ContentInteraction)
admin.site.register(CourseProgress)
admin.site.register(FavoriteContent)