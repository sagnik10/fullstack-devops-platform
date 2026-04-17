from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns=[
path("admin/",admin.site.urls),
path("",include("core.urls")),
path("courses/",include("courses.urls")),
path("articles/",include("articles.urls")),
path("dashboard/",include("automation.urls")),
path("accounts/",include("allauth.urls")),
path("accounts/",include("accounts.urls"))
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)