from django.urls import path
from .views import HomePageView, AboutPageView, PagePageView


urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('about/', AboutPageView.as_view(), name = 'about'),
    path('page/', PagePageView.as_view(), name = 'page')
]