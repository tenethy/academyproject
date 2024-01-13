from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import PostArticle, Category

# Create your views here.

class HomePageView(ListView):
    model = PostArticle
    template_name = "home.html"

def TodaysNewsView(request):
    first_article = PostArticle.objects.first()
    third_article = PostArticle.objects.all()[1:3]
    return render(request,"Todaysection/todaysnews.html",{
        'first_article':first_article,
        'third_article':third_article,
        })

def BreakingNewsView(request):
    return render(request, "Todaysection/breakingnews.html")

def SportsPageView(request):
    post_by_category = PostArticle.objects.filter(category=Category.objects.get(title = 'sports'))
    return render(request, "Explore/sports.html", {
        'post_by_category':post_by_category
        })

class PopCulturePageView(ListView):
    model = PostArticle
    template_name = "Explore/popculture.html"

class LocalNewsPageView(ListView):
    model = PostArticle
    template_name = "Explore/localnews.html"

class LifeStylePageView(ListView):
    model = PostArticle
    template_name = "Explore/lifestyle.html"

class InternationalNewsPageView(ListView):
    model = PostArticle
    template_name = "Explore/internationalnews.html"

class FinancePageView(ListView):
    model = PostArticle
    template_name = "Explore/finance.html"

class BusinessPageView(ListView):
    model = PostArticle
    template_name = "Explore/business.html"

class ArchivesPageView(ListView):
    model = PostArticle
    template_name = "Explore/archives.html"