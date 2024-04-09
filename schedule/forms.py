from django import forms
from .models import MyEvent

class MyEventForm(forms.ModelForm):
    class Meta:
        model = MyEvent
        fields = ['title', 'date', 'location', 'description']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'date'}),
        }
