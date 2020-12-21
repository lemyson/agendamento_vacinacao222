from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


    def _str_(self):
        return self.title

    def get_absolute_url(self):
        return reverse("agen:detail", kwargs={"slug": self.slug})



