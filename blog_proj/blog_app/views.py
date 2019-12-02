from django.shortcuts import render
from .models import Post
from django.views.generic import (ListView,
DetailView,
CreateView
)

# def home(request):
#     context = {
#         'posts': Post.objects.all()
#         }
#     return render(request, 'blog_app/home.html', context)

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name='blog_app/home.html'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']


def about(request):
    return render(request, 'blog_app/about.html',{'title':'About'})
