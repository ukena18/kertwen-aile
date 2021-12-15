from . import views
from django.urls import path
# our custom views powered by django.views.generic
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    UserPostListView)

urlpatterns = [
    #
    path("", PostListView.as_view(), name="blog-home"),
    path("user/<str:username>", UserPostListView.as_view(), name="blog-user"),
    # built-in views and url path
    path("post/<int:pk>/", PostDetailView.as_view(), name="blog-detail"),
    # built-in views and url path
    path("post/new/", PostCreateView.as_view(), name="blog-create"),
    # built-in views and url path
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="blog-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="blog-delete"),
    path("about/", views.about, name="blog-about"),
    path("comment/<int:pk>/",views.comment, name="blog-comment"),
]