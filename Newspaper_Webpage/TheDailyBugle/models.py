from django.db import models
from turtle import title

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length = 200, null = True)
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.title

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