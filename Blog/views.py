from django.http import Http404
from django.shortcuts import render

posts = [
    {
        'id': 1,
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'first post',
        'date_posted': '31 oct 2026'
    },
    {
        'id': 2,
        'author': 'Mansi Gharat',
        'title': 'Blog Post 2',
        'content': 'Second post',
        'date_posted': '30 oct 2026'
    },
    {
        'id': 3,
        'author': 'John Deo',
        'title': 'Blog Post 3',
        'content': 'Third post',
        'date_posted': '29 oct 2026'
    }
]

def home(request):
    return render(request, 'Blog/home.html', {'posts': posts})

def about(request):
    return render(request, 'Blog/about.html', {'title': 'About'})

def post_detail(request, post_id):
    for post in posts:
        if post['id'] == post_id:
            return render(request, 'Blog/post_detail.html', {'post': post})
    raise Http404("Post not found")