from django.forms import ModelForm
from django import forms
from .models import *


class BirthForm(ModelForm):
    class Meta:
        model = Birth
        fields = '__all__'