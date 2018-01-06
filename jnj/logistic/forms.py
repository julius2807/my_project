from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class PriceQueryForRentalForm(forms.Form):
    cargo_type_id = forms.CharField(max_length=255, required=True)
    transport_service_id = forms.CharField(max_length=255, required=True)
    transport_id = forms.CharField(max_length=255, required=True)
    origin = forms.CharField(max_length=1000, required=True)
    destination = forms.CharField(max_length=1000, required=True)
    distance = forms.CharField(max_length=20)
    duration = forms.CharField(max_length=20)

class PriceQueryForPackageForm(forms.Form):
    drop_to_branch = forms.CharField(max_length=5, required=True)
    origin = forms.CharField(max_length=1000, required=True)
    destination = forms.CharField(max_length=1000, required=True)
    volume_length = forms.CharField(max_length=20, required=True)
    volume_width = forms.CharField(max_length=20, required=True)
    volume_height = forms.CharField(max_length=20, required=True)
    weight = forms.CharField(max_length=20, required=True)
    distance = forms.CharField(max_length=20)
