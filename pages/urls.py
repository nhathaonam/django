from django.urls import path

from .views import HomePageView, AboutView, HomeBase

urlpatterns = [
    path("", HomeBase.as_view(), name = "base"),
    path('home/', HomePageView.as_view(), name = 'home'),
    path('about/', AboutView.as_view(), name = 'about')
]