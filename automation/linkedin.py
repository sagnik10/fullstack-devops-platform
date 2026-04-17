from automation.models import LinkedInPost
from articles.models import Article

def generate():
articles=Article.objects.filter(published=True).order_by("-created")[:1]
for a in articles:
LinkedInPost.objects.create(
title=a.title,
content=a.content
)
