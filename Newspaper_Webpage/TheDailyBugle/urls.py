from django.urls import path
from .views import HomePageView, TodaysNewsView, BreakingNewsView, SportsPageView, PopCulturePageView, LocalNewsPageView, LifeStylePageView, InternationalNewsPageView, FinancePageView, BusinessPageView, ArchivesPageView

app_name = 'TheDailyBugle'
urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('todaysnews/', TodaysNewsView.as_view(), name = 'todaysnews'),
    path('breakingnews/', BreakingNewsView.as_view(), name = 'breakingnews'),
    path('sportsnews/', SportsPageView.as_view(), name = 'sportsnews'),
    path('popculturenews/', PopCulturePageView.as_view(), name = 'popculturenews'),
    path('localnews/', LocalNewsPageView.as_view(), name = 'localnews'),
    path('lifestylenews/', LifeStylePageView.as_view(), name = 'lifestylenews'),
    path('internationalnews/', InternationalNewsPageView.as_view(), name = 'internationalnews'),
    path('financenews/', FinancePageView.as_view(), name = 'financenews'),
    path('businessnews/', BusinessPageView.as_view(), name = 'businessnews'),
    path('archive/', ArchivesPageView.as_view(), name = 'archive'),
]