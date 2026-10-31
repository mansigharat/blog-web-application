from django.http import HttpResponse
from django.shortcuts import render
posts = [
    {
        'author' :'CoreyMS',
        'title' : 'Blog Post 1',
        'content' : 'first post',
        'date_posted' : '31 oct 2026'
    },
    {
            'author' :'Mansi Gharat',
            'title' : 'Blog Post 2',
            'content' : 'Second post',
            'date_posted' : '30 oct 2026'
    },
    {
            'author' :'John Deo',
            'title' : 'Blog Post 3',
            'content' : 'Third post',
            'date_posted' : '29 oct 2026'
    }
]
def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'Blog/home.html', context)

def about(request):
    return render(request, 'Blog/about.html', {'title' : 'About'})
