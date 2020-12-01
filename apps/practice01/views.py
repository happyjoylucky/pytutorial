from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogPracticeForm

# Create your views here.
from .models import BlogPractice
from django.utils import timezone


def post_list(request):
    posts = BlogPractice.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'practice01/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(BlogPractice, pk=pk)
    return render(request, 'practice01/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = BlogPracticeForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post = form.save()
            return redirect('practice01:post_detail', pk=post.pk)
    else:
        form = BlogPracticeForm()
    return render(request, 'practice01/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(BlogPractice, pk=pk)
    if request.method == "POST":
        form = BlogPracticeForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('practice01:post_detail', pk=post.pk)
    else:
        form = BlogPracticeForm(instance=post)
    return render(request, 'practice01/post_edit.html', {'form': form})


