from attr import field
from django import forms
from .models import *

class Send(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'