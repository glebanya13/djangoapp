from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import FormView, ListView

from .models import Hotel

from .forms import HotelForm

class HomePageView(FormView):
    form_class = HotelForm
    template_name = 'index.html'

class HotelsPageView(ListView):
    model = Hotel
    template_name = 'hotels.html'

    def get_queryset(self):
        name = self.request.GET.get("name")
        country = self.request.GET.get("country")
        object_list =  Hotel.objects.filter(
            Q(name__icontains=name) | Q(country__icontains=country)
        )
        return object_list