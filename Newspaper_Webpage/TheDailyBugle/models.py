from django.db import models
from django.db import models
from pyexpat import model
from turtle import title
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, null = True)
    author = models.ForeignKey(
        "auth.User",
        on_delete = models.CASCADE,
        null = True,
    )

    body = models.TextField(default = timezone.now)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("zeeeee:post_details", kwargs={"pk":self.pk})