from django.db import models


# Create your models here.
class Article(models.Model):
    article_title = models.CharField(max_length=100)
    article_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
