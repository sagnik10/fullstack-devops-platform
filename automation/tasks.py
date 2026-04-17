from celery import shared_task
from .services import generate_article
from .models import GeneratedArticle

@shared_task
def create_daily_article():

    content=generate_article("DevOps CI/CD pipeline")

    GeneratedArticle.objects.create(
        title="Automated DevOps Article",
        content=content
    )
