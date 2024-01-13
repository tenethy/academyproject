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
    path('popculturenews/', PopCulturePageView.as_view(), name = 'popculturenews'),
    path('localnews/', LocalNewsPageView.as_view(), name = 'localnews'),
    path('lifestylenews/', LifeStylePageView.as_view(), name = 'lifestylenews'),
    path('internationalnews/', InternationalNewsPageView.as_view(), name = 'internationalnews'),
    path('financenews/', FinancePageView.as_view(), name = 'financenews'),
    path('businessnews/', BusinessPageView.as_view(), name = 'businessnews'),
    path('archive/', ArchivesPageView.as_view(), name = 'archive'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)