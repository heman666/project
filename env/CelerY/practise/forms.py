from django import forms
from .models import Info

class Info_form(forms.ModelForm):
    class Meta:
        model = Info
        fields = '__all__'
