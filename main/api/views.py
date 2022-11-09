from rest_framework.generics import ListAPIView

from .serializers import HotelSerializer
from main.models import Hotel


class ListHotelsView(ListAPIView):
	serializer_class = HotelSerializer
	queryset = Hotel.objects.all()
