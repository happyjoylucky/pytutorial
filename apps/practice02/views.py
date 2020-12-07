from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import Post02Form
from .models import Post02


def post_list(request):
    posts = Post02.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'practice02/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post02, pk=pk)
    return render(request, 'practice02/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = Post02Form(request.POST)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.published_date = timezone.now()
            newpost = form.save()
            return redirect('practice02:post_detail', pk=newpost.pk)
    else:
        form = Post02Form()
    return render(request, 'practice02/post_edit.html', {'form': form})


def post_edit(request, pk):
    editpost = get_object_or_404(Post02, pk=pk)
    if request.method == "POST":
        form = Post02Form(request.POST, instance=editpost)
        if form.is_valid():
            editpost = form.save(commit=False)
            editpost.author = request.user
            editpost.published_date = timezone.now()
            editpost = form.save()
            return redirect('practice02:post_detail', pk=editpost.pk)
    else:
        form = Post02Form(instance=editpost)
    return render(request, 'practice02/post_edit.html', {'form': form})
