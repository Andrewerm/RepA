from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from django.views.generic import View
from .models import Post, Tag
from django.shortcuts import render, redirect, reverse
from .forms import TagForm, PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

class PostDetail(ObjectDetailMixin, View):
    model=Post
    template = 'blog/post_detail.html'


class TagDetail(ObjectDetailMixin,View):
    model=Tag
    template = 'blog/tag_detail.html'

# Create your views here.
def posts_list(request):
    posts=Post.objects.all()
    paginator=Paginator(posts, 2)
    page_number=request.GET.get('page',1)
    page=paginator.get_page(page_number)
    return render(request, "blog/index.html", context={'page_ojects':page})


def tags_list(request):
    tags=Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})

class TagCreate(LoginRequiredMixin,ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True

class TagUpdate(LoginRequiredMixin,ObjectUpdateMixin,View):
    form_model = TagForm
    template = 'blog/tag_update_form.html'
    model = Tag
    raise_exception = True


class PostUpdate(LoginRequiredMixin,ObjectUpdateMixin,View):
    form_model = PostForm
    template = 'blog/post_update_form.html'
    model = Post
    raise_exception = True


class PostCreate(LoginRequiredMixin,ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create.html'
    raise_exception = True

class TagDelete(LoginRequiredMixin,ObjectDeleteMixin, View):
    template='blog/tag_delete.html'
    model=Tag
    redirect_url = 'tags_list_url'
    raise_exception = True

class PostDelete(LoginRequiredMixin,ObjectDeleteMixin, View):
    template='blog/post_delete.html'
    model=Post
    redirect_url='posts_list_url'
    raise_exception = True
