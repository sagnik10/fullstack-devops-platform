from django import forms
from courses.models import Course
from articles.models import Article

class CourseForm(forms.ModelForm):
    class Meta:
        model=Course
        fields=["title","thumbnail","content","link","metadata"]

class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=["title","thumbnail","content","link","metadata"]
