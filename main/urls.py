from django.urls import path
from .views import HomePageView, HotelsPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('hotels', HotelsPageView.as_view(), name='hotels'),
]