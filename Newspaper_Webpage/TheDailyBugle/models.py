from django.db import models
from turtle import title
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length = 200, null = True)
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.title

class User_Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete = models.CASCADE)

    user_name = models.CharField(max_length=200, null = True)

    profile_image = models.ImageField(upload_to ='profilepic/', null=True)

    bio = models.TextField(null = True, blank = True)

    def __str__(self) -> str:
        return str(self.user)

class PostArticle(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE, null = True)

    title = models.CharField(max_length=200, null = True)

    author = models.ForeignKey(
        "auth.User",
        on_delete = models.CASCADE,
        null = True,
    )

    category_image = models.ImageField(upload_to ='articles/')

    article_body = models.TextField(null = True, blank = True)

    date_time = models.DateTimeField(auto_now_add = True)

    location = models.CharField(max_length=200, null = True)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("TheDailyBugle:post_details", kwargs={"pk":self.pk})