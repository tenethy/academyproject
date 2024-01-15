from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import PostArticle, Category, User_Profile

# Create your views here.

def HomePageView(request):
    employee_pfp = User_Profile.objects.all()
    return render(request, "home.html", {
        'employee_pfp':employee_pfp
        })

def TodaysNewsView(request):
    latest_articles = PostArticle.objects.filter(category=Category.objects.get(title = 'International')).latest('date_time'), PostArticle.objects.filter(category=Category.objects.get(title = 'Sports')).latest('date_time'), PostArticle.objects.filter(category=Category.objects.get(title = 'Local')).latest('date_time'), PostArticle.objects.filter(category=Category.objects.get(title = 'Life style')).latest('date_time'), PostArticle.objects.filter(category=Category.objects.get(title = 'Pop culture')).latest('date_time'), PostArticle.objects.filter(category=Category.objects.get(title = 'Finance')).latest('date_time'), PostArticle.objects.filter(category=Category.objects.get(title = 'Business')).latest('date_time')
    return render(request,"Todaysection/todaysnews.html",{
        'latest_articles':latest_articles,
        })

def BreakingNewsView(request):
    return render(request, "Todaysection/breakingnews.html")

def SportsPageView(request):
    post_by_category = PostArticle.objects.filter(category=Category.objects.get(title = 'Sports'))
    return render(request, "Explore/sports.html", {
        'post_by_category':post_by_category,
        })

def PopCulturePageView(request):
    post_by_category = PostArticle.objects.filter(category=Category.objects.get(title = 'Pop culture'))
    return render(request, "Explore/popculture.html", {
        'post_by_category':post_by_category,
        })

def LocalNewsPageView(request):
    post_by_category = PostArticle.objects.filter(category=Category.objects.get(title = 'Local'))
    return render(request, "Explore/localnews.html", {
        'post_by_category':post_by_category,
        })

def LifeStylePageView(request):
    post_by_category = PostArticle.objects.filter(category=Category.objects.get(title = 'Life style'))
    return render(request, "Explore/lifestyle.html", {
        'post_by_category':post_by_category,
        })

def InternationalNewsPageView(request):
    post_by_category = PostArticle.objects.filter(category=Category.objects.get(title = 'International'))
    return render(request, "Explore/internationalnews.html", {
        'post_by_category':post_by_category,
        })

def FinancePageView(request):
    post_by_category = PostArticle.objects.filter(category=Category.objects.get(title = 'Finance'))
    return render(request, "Explore/finance.html", {
        'post_by_category':post_by_category,
        })

def BusinessPageView(request):
    post_by_category = PostArticle.objects.filter(category=Category.objects.get(title = 'Business'))
    return render(request, "Explore/business.html", {
        'post_by_category':post_by_category,
        })

class ArchivesPageView(ListView):
    model = PostArticle
    template_name = "Explore/archives.html"

class PostDetailsPageView(DetailView):
    model = PostArticle
    template_name = "PostFunctions/post_details.html"