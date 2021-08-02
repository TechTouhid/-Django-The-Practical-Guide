from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting_page"),
    path("posts", views.posts, name="posts_detail"),
    path("posts/<slug:slug>", views.post_details, name="posts_detail-page")  # /posts/my-first-post
]
