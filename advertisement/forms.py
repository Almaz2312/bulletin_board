from django import forms
from .models import Advertisement, AdvertisementImage


class AdvertisementForm(forms.ModelForm):
    """Advertisement form"""

    class Meta:
        model = Advertisement
        fields = [
            'title',
            'description',
        ]


class AdvertisementImageForm(forms.ModelForm):
    """Advertisement image form"""
    class Meta:
        model = AdvertisementImage
        fields = [
            'image',
        ]
