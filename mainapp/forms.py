from django import forms

from mainapp.models import Category, Post


class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'text', 'image', 'user')

class EditPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'text', 'image', 'user')

