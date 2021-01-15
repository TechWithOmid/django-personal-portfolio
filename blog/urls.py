from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.blog_post, name="blog_post"),
    path('<int:post_id>', views.detail, name="detail"),
]