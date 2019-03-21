import random
from django.shortcuts import render, get_object_or_404
from entry.models import Post


def list(request):

    posts = Post.objects.filter(is_published=True).order_by('-created_at')

    context = {
            'posts': posts,
        }
    return render(request, 'lesson/list.html', context)


def detail(request, pk, slug):
    post = get_object_or_404(Post, pk=pk, is_published=True)

    context = {
            'post': post,
        }
    return render(request, 'lesson/detail.html', context)
