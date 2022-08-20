from dataclasses import fields
from django import forms
from .models import Painting

class PaintingCreateForm(forms.ModelForm):
    class Meta:
        model = Painting
        fields = ["name", "discription", "author", "size", "subject", "price", "image"]
