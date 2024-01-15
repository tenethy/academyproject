from django.contrib import admin
from .models import Category, PostArticle, User_Profile

# Register your models here.

admin.site.register(Category)
class AdminPostArticle(admin.ModelAdmin):
    list_display = ('title','date_time')
admin.site.register(PostArticle,AdminPostArticle)
admin.site.register(User_Profile)