from django.urls import path

from .views import HotelsListView, HotelsCreateView

urlpatterns = [
    path('manager/', HotelsListView.as_view()),
    path('create/', HotelsCreateView.as_view())
]
