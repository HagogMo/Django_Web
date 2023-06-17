from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post


# list views for which group I'm signed up for
# Create your views here.
def home(request) :
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'commun/home.html', context)

class PostListView(ListView) :
    model = Post
    template_name = 'commun/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView) :
    model = Post

def about(request) :
    return render(request, 'commun/about.html')