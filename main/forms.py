from .models import Hotel
from django.forms import ModelForm, TextInput, ChoiceField


class HotelForm(ModelForm):
    class Meta:
        CHOICES = (('Option 1', 'Россия'), ('Option 2', 'Россия'),)
        country = ChoiceField(choices=CHOICES),

        model = Hotel
        fields = ["name", "country"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'name': 'name',
                'placeholder': 'Название'
            }),
        }
