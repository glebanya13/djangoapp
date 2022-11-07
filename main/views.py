from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import FormView, ListView

from .models import Hotel

from .forms import HotelForm

class HomePageView(FormView):
    form_class = HotelForm
    template_name = 'index.html'
    success_url = '/hotels'
    failed_url = '/home'

    def form_valid(self, form):
        name = form.cleaned_data.get("name")
        country = form.cleaned_data.get("country")
        
        obj =  Hotel.objects.filter(
            Q(name__icontains=name) | Q(country__icontains=country)
        )

        return redirect(reverse_lazy('hotels'), hotels=obj)
    

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