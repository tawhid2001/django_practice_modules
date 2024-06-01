from django import forms
from .models import albumsModel

class albumForm(forms.ModelForm):
    class Meta:
        model = albumsModel
        fields = '__all__'

        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }

