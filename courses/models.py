from django.db import models

class Course(models.Model):
    title=models.CharField(max_length=200)
    thumbnail=models.ImageField(upload_to="thumbnails/",blank=True,null=True)
    content=models.TextField(blank=True)
    link=models.URLField(default="https://example.com")
    metadata=models.TextField(blank=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
