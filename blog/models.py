from time import strftime

from django.db import models
from django.db.models import Model
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User



class Post(Model):
    title = models.CharField(max_length=255, null=False)
    content = models.CharField(max_length=255, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(default='default.jpeg', upload_to='post_image/')
    
    def __str__(self):
        return f'title: {self.title}\ author: {self.author}'

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})





