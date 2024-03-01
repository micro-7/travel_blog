from django import forms
from .models import blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = ('title', 'author_name','category' ,'description', 'image')