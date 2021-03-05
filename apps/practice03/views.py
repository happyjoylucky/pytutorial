from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post03

# Create your views here.


def post_list(request):
    posts = Post03.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'practice03/post_list.html', {"posts": posts})

def post_detail(request, pk):
    post = get_object_or_404(Post03, pk)
    return render(request, 'practice03/post_detail.html', {"post": post})
