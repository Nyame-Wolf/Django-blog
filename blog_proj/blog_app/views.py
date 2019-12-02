from django.shortcuts import render
from .models import Post
from django.views.generic import (ListView,
DetailView,
CreateView,
UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin

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

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'blog_app/about.html',{'title':'About'})
