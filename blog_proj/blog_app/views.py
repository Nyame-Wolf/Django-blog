from django.shortcuts import render
from .models import Post
from django.views.generic import (ListView,
DetailView,
CreateView,
UpdateView,
DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# def home(request):
#     context = {
#         'posts': Post.objects.all()
#         }
#     return render(request, 'blog_app/home.html', context)

#refactor the above home view func as a CBV.
class PostListView(ListView):
    model = Post
    context_object_name = 'posts' # tell django name we have used in our template. otherwise use django default 'object'
    template_name='blog_app/home.html' #django default naming convention is  <app>/<model>_<viewtype>.html
    ordering = ['-date_posted'] # to order posts. since we want newest first we use -ve 

class PostDetailView(DetailView):
    model = Post

#LoginRequired mixin requires that a user must be an account holder to create a post. Redirects logged out users to login page
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    #this method sets the author field of our model
    #overrides the form_valid method by taking form we are submitting and setting its instance to current logged in user
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#uses same form as CreateView. We add a UserPassesTestMixin to ensure that its only posts authors who can update posts
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #uses UserPassesTestMixin
    def test_func(self):
        post = self.get_object()# .get_object() returns exact post we are editing
        return self.request.user == post.author #checks that posts authors can update posts. raises a 403 forbidden for not authors

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/' # this redirects back to homepage when a post is succesfully deleted
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


def about(request):
    return render(request, 'blog_app/about.html',{'title':'About'})
