from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=60)
    content = models.CharField(max_length=500)
    postdate = models.DateTimeField(auto_now_add=True)
    lastmodifieddate = models.DateTimeField(auto_now=True)
    numberofhits = models.IntegerField(default=0)