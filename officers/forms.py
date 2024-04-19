from django import forms
from .models import Events

class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = '__all__'
        exclude = ['user ']

        widgets = {
            'time_start':forms.TextInput(attrs={'type':'datetime-local','id':'time_start'}),
            'time_end':forms.TextInput(attrs={'type':'datetime-local','id':'time_end'}),
            'poster': forms.ClearableFileInput(attrs={'class': 'block w-full text-md text-gray-900 border border-gray-300 rounded-lg cursor-pointer file:bg-gray-700 file:text-white file:p-2'}),

        }