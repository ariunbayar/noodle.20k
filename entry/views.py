import markdown
from django.shortcuts import render, redirect, get_object_or_404
from entry.forms import PostForm
from entry.models import Post


def list(request):

    posts = Post.objects.all().order_by('-created_at')

    context = {
            'posts': posts,
        }

    return render(request, 'entry/list.html', context)


def form(request, pk=None):

    if pk:
        post = get_object_or_404(Post, pk=pk)
    else:
        post = None

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            if not post:
                post = Post()
            post.title = form.cleaned_data.get('title')
            post.content = form.cleaned_data.get('content')
            post.content_html = markdown.markdown(post.content)
            post.save()
            return redirect('entry-detail', post.id)
    else:
        form = PostForm(initial={
                'title': post.title if post else '',
            })

    context = {
            'form': form,
            'post': post,
        }

    return render(request, 'entry/form.html', context)


def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('entry-list')


def publish_toggle(request, pk, is_published):
    post = get_object_or_404(Post, pk=pk)
    post.is_published = is_published
    post.save()
    return redirect('entry-detail', post.id)


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
            'post': post,
        }
    return render(request, 'entry/detail.html', context)
