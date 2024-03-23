from django import forms
from .models import Post

class PostForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = [
           'author',
           'categoryType',
           #'postCategory',
           'title',
           'text',

       ]

class SearchForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'category',
            'dateCreation',
        ]
