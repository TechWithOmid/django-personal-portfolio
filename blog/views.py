from django.shortcuts import render, get_object_or_404
from .models import Post


def blog_post(request):
    posts = Post.objects.order_by('-date')  # order the blog post by date and it will show the last 5 post
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})
