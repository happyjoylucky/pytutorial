from django.forms import ModelForm
from .models import BlogPractice


class BlogPracticeForm(ModelForm):

    class Meta:
        model = BlogPractice
        fields = ('title', 'text')