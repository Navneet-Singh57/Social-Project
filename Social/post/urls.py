from django.urls import path
from . import views

urlpatterns = [
    path('post-create/',views.PostCreate,name="post_create"),
    path('feed/',views.feed,name="feed"),
    path('like/',views.like_post,name="like"),
] 