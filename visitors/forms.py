from django import forms
from .models import Request
 
class Requestform(forms.ModelForm):
 
    class Meta:
        model = Request
        fields = ('Name','Phone','Email', 'Special_request')
