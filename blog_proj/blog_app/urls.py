# this contains urls which map blog_app view funcs and CBV.
from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)
from .feeds import LatestPostsFeed

urlpatterns = [
    path("", views.home, name="blog-home"),
    path("tag/<slug:tag_slug>/", views.home, name="post_list_by_tag"),
    # path('',PostListView.as_view(), name='blog-home'),
    path("user/<str:username>/", UserPostListView.as_view(), name="user-posts"),
    # path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail'), # contains a variable pk-stands for priamry key which heplps access a specific post
    path("post/<int:pk>/", views.post_detail, name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("about/", views.about, name="blog-about"),
    path("post/<int:post_id>/share/", views.post_share, name="post_share"),
    path("feed/", LatestPostsFeed(), name="post_feed"),
]
