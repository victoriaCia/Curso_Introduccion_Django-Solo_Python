from dataclasses import field
from socket import fromshare
from django import forms
from .models import Post

#creación de un formulario para crear post desde la app usando el modelo Post
class PostCreateForm(forms.ModelForm):   
    class Meta:
        model=Post
        fields=('title','content')