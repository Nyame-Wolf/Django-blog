# this contains urls which map blog_app view funcs and CBV. 
from django.urls import path
from . import views
from .views import (PostListView,
PostDetailView,
PostCreateView,
PostUpdateView,
PostDeleteView)

urlpatterns = [
    #path('',views.home, name='blog-home'),
    path('',PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail'), # contains a variable pk-stands for priamry key which heplps access a specific post
    path('post/new/',PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post-delete'),
    path('about/',views.about, name='blog-about'),

]
