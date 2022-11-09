from rest_framework import serializers

from main.models import Hotel


class HotelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Hotel
		fields = ("id", "name", "country", "stars",)
