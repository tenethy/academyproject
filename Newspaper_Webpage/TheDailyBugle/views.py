from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = "home.html"

class TodaysNewsView(ListView):
    model = Post
    template_name = "Todaysection/todaysnews.html"

class BreakingNewsView(ListView):
    model = Post
    template_name = "Todaysection/breakingnews.html"

class SportsPageView(ListView):
    model = Post
    template_name = "Explore/sports.html"

class PopCulturePageView(ListView):
    model = Post
    template_name = "Explore/popculture.html"

class LocalNewsPageView(ListView):
    model = Post
    template_name = "Explore/localnews.html"

class LifeStylePageView(ListView):
    model = Post
    template_name = "Explore/lifestyle.html"

class InternationalNewsPageView(ListView):
    model = Post
    template_name = "Explore/internationalnews.html"

class FinancePageView(ListView):
    model = Post
    template_name = "Explore/finance.html"

class BusinessPageView(ListView):
    model = Post
    template_name = "Explore/business.html"

class ArchivesPageView(ListView):
    model = Post
    template_name = "Explore/archives.html"