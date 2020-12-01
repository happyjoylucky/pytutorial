from django import forms
from .models import BlogPractice


class BlogPracticeForm(forms.ModelForm):

    class Meta:
        model = BlogPractice
        fields = ('title', 'text')