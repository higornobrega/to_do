from django import forms
from django.db import models
from django.db.models import fields
from django.db.models.fields import Field
from .models import TarefaBd

class ContentForm(forms.ModelForm):
    class Meta:
        model = TarefaBd
        fields = ['content']