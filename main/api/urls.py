from django.urls import path

from .views import ListHotelsView


urlpatterns = [
    path('hotels', ListHotelsView.as_view(), name='hotels_list'),
]
