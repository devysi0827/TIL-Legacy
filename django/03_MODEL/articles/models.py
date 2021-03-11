from django.db import models

# Create your models here.
class Article(models.Model):
    #id-자동 title:col content
    #charfield =>길이제한이 있는 텍스트
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
