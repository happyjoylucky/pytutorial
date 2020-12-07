from django.forms import ModelForm
from .models import Post02


class Post02Form(ModelForm):

    class Meta:
        model = Post02
        fields = ['title', 'text']