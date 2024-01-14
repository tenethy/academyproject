from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageView, TodaysNewsView, BreakingNewsView, SportsPageView, PopCulturePageView, LocalNewsPageView, LifeStylePageView, InternationalNewsPageView, FinancePageView, BusinessPageView, ArchivesPageView
from . import views

app_name = 'TheDailyBugle'
urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('todaysnews/', views.TodaysNewsView, name = 'todaysnews'),
    path('breakingnews/', views.BreakingNewsView, name = 'breakingnews'),
    path('sportsnews/', views.SportsPageView, name = 'sportsnews'),
    path('popculturenews/', views.PopCulturePageView, name = 'popculturenews'),
    path('localnews/', views.LocalNewsPageView, name = 'localnews'),
    path('lifestylenews/', views.LifeStylePageView, name = 'lifestylenews'),
    path('internationalnews/', views.InternationalNewsPageView, name = 'internationalnews'),
    path('financenews/', views.FinancePageView, name = 'financenews'),
    path('businessnews/', views.BusinessPageView, name = 'businessnews'),
    path('archive/', ArchivesPageView.as_view(), name = 'archive'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)