from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import TemplateView, ListView

from .models import Hotel

class HomePageView(TemplateView):
    template_name = 'index.html'

class HotelsPageView(ListView):
    model = Hotel
    template_name = 'hotels.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list =  Hotel.objects.filter(
            Q(name__icontains=query) | Q(country__icontains=query)
        )
        return object_list