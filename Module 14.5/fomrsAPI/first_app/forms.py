from django import forms
from django.forms.widgets import NumberInput

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class TestForm(forms.Form):
    name = forms.CharField(max_length=20)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows' : 3}))
    roll = forms.IntegerField(help_text='Please enter 6 digits')
    email = forms.EmailField(label="please enter your email")
    pasword = forms.CharField(widget= forms.PasswordInput())
    dob = forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    fabCol1 = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    fabCol2 = forms.ChoiceField(widget=forms.RadioSelect,choices=FAVORITE_COLORS_CHOICES)
    agree = forms.BooleanField()