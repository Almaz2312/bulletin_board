from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
# from .models import User

User = get_user_model()


class SignupForm(UserCreationForm):
    username = forms.CharField(min_length=3, max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    city = forms.CharField(max_length=30, required=False)
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'city', 'phone', 'avatar')
