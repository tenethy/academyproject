from django.urls import path
from .views import SubscribePageView

app_name = 'accounts'
urlpatterns = [
    path('subscribe/', SubscribePageView.as_view(), name = 'subscribe'),
]