from django.shortcuts import render, get_object_or_404
from .models import Post



# Create your views here.
def posts_list(request):
    posts=Post.objects.all()
    return render(request, "blog/index.html", context={'posts':posts} )

def post_detail(request, slug):
    post=get_object_or_404(Post, slug__iexact=slug)
    return (render(request, 'blog/post_detail.html', {'post':post}))
