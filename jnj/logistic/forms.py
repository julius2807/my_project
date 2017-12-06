from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class PriceQueryForm(forms.Form):
    cargo_type_id = forms.CharField(max_length=255, required=True)
    transport_service_id = forms.CharField(max_length=255, required=True)
    transport_id = forms.CharField(max_length=255, required=True)
    origin = forms.CharField(max_length=1000, required=True)
    destination = forms.CharField(max_length=1000, required=True)
    distance = forms.CharField(max_length=20)
    duration = forms.CharField(max_length=20)
