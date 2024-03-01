from os import name
from django.db import models
from django.db.models.fields import CharField, DateTimeField, EmailField, TextField, URLField

class blog(models.Model):
    title = CharField(max_length=50)
    date = DateTimeField(auto_now=True)
    category = CharField(max_length=35)
    author_name = CharField(max_length=30)
    description = TextField()
    image = models.ImageField(upload_to='blog')

    class Meta:

        verbose_name = 'blog'
        verbose_name_plural = 'blogs'

    def __str__(self):
        return self.title
