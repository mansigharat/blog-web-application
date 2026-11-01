from django.http import Http404
from django.shortcuts import render
from .models import Post
post_var = Post.objects.all()
def home(request):
    return render(request, 'Blog/home.html', {'posts': post_var})

def about(request):
    return render(request, 'Blog/about.html', {'title': 'About'})

def landing(request):
    return render(request, 'Blog/landing_page.html', {'posts': post_var, 'title': 'Welcome'})

def post_detail(request, post_id):
    for post in post_var:
        if post['id'] == post_id:
            return render(request, 'Blog/post_detail.html', {'post': post})
    raise Http404("Post not found")