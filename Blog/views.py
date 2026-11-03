
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, 'Blog/home.html', {'posts': posts})


def about(request):
    return render(request, 'Blog/about.html', {'title': 'About'})


def landing(request):
    posts = Post.objects.all()
    return render(request, 'Blog/landing_page.html', {
        'posts': posts,
        'title': 'Welcome'
    })


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'Blog/post_detail.html', {'post': post})
