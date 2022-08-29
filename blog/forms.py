from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'blog_pic')
        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control  row mb-3', 'placeholder': 'Title'}),
            'description': forms.TextInput(attrs={'class': 'form-control  row mb-3', 'placeholder': 'Description'})


        }

        labels = {"title": "Title", "description": "Description",
                  'blog_pic': 'Profile Picture'}
