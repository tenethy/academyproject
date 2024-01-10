from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

class SubscribePageView(CreateView):
    form_class = UserCreationForm
    success_urls = reverse_lazy("TheDailyBugle:home")
    template_name = "registration/subscribe.html"