from django.shortcuts import render, redirect

from .models import Hotel

def index(request):
    if request.method == "POST":
        searched = request.POST['searched']
        country = request.POST['country']

        print(searched)
        print('--------')
        print(country)
        print('--------')
        print(Hotel.objects.all())

        hotels = Hotel.objects.filter(name__contains=searched)
        
        # return render(request, 'main/index.html', {'title': 'Home'})
        
    else:
        return render(request, 'main/index.html', {'title': 'Home'})

def hotels(request):
    return render(request, 'main/hotels.html', {'title': 'Hotels'})