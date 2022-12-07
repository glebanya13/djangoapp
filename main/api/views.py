from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny

from .serializers import HotelSerializer
from ..models import Hotel

from rest_framework import status
from rest_framework.response import Response


class HotelsListView(ListAPIView):
    queryset = Hotel.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = HotelSerializer


class HotelsCreateView(CreateAPIView):
    queryset = Hotel.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = HotelSerializer
