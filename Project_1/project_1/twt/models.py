from django.db import models

# Create your models here.
class Tweet(models.Model):
    id = models.TextField(primary_key=True)
    text_content = models.TextField()
    url = models.TextField()

    def __init__(self, id='', text_content='', url=''):
        self.id = id
        self.text_content = text_content
        self.url = url

    def log_information(self):
        return f'Id: {self.id}. Text_content: {self.text_content}. Url: {self.url}'
