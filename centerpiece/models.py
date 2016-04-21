from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    url = models.URLField(primary_key=True)
    text = models.TextField()
    
    def __str__(self):
        return str(url)
# Create your models here.
