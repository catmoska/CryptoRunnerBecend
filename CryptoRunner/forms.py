from django import forms
from .models import *

class NewForms(forms.Form):
    colisestvo = forms.IntegerField()
    # startSislo = forms.IntegerField()
    stoimostStart = forms.FloatField()
    Neriod = forms.FloatField()
    Tip = forms.IntegerField()
