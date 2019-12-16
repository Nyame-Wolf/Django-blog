from django.shortcuts import render,get_object_or_404
from .models import Post
from django.views.generic import (ListView,
DetailView,
CreateView,
UpdateView,
DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
from .forms import EmailPostForm
from django.core.mail import send_mail


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
    paginate_by = 5 #Ensures we have five posts per page. pagination logic i.e to create links to other pages, we do it in  the homepage template

#to return paginated posts by a user. uses user_posts.html template. filtering is done by url by specifying username
class UserPostListView(ListView):
    model = Post
    context_object_name = 'posts' # tell django name we have used in our template. otherwise use django default 'object'
    template_name='blog_app/user_posts.html' #django default naming convention is  <app>/<model>_<viewtype>.html
    # this gets overrode by the get_queryset method so we set it there ordering = ['-date_posted'] 
    paginate_by = 5 #Ensures we have five posts per page. pagination logic i.e to create links to other pages, we do it in  the homepage template

    #to modify queryset returned by this view , we override a method get_queryset 
    def get_queryset(self):
        #to get user assosciated with username we shall get username from url. if user doest exist  a 404 error is raised
        user = get_object_or_404(get_user_model(), username=self.kwargs.get('username'))# kwargs rep query parameters
        return Post.objects.filter(author=user).order_by('-date_posted')# the overrode ordering

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

#Add a post sharing by email functionality
def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f'{cd["name"]} ({cd["email"]}) recommends you reading "{post.title}"'
            message = f'Read "{post.title}" at {post_url}\n\n{cd["name"]}\'s comments: {cd["comments"]}'
            send_mail(subject, message, 'admin@myblog.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog_app/post_share.html', {'post':post, 'form':form, 'sent':sent})
    
