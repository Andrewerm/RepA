from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DateDetailView
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail

# Create your views here.


class Post_list(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'



def post_detail(request, year, month, day, post):
     post=get_object_or_404(Post, slug=post, status='published', publish__year=year,
                            publish__month=month, publish__day=day)
     comments=post.comment.filter(active=True)
     new_comment=None
     if request.method=='POST':
         form = CommentForm(data=request.POST)
         if form.is_valid():
             new_comment=form.save(commit=False)
             new_comment.post=post
             new_comment.save()
     else:
         form=CommentForm()
     return render(request, 'blog/post/detail.html',
                   context={'post':post, 'comments':comments, 'form':form})

def post_share(request, post_id):
    # Получение статьи по идентификатору
    post=get_object_or_404(Post, id=post_id, status='published' )
    sent = False
    if request.method=='POST':
        #   Форма была отправлена на сохранение.
        form = EmailPostForm(request.POST)

        if form.is_valid():
        # Все поля формы прошли валидацию
            cd = form.cleaned_data
            # ... Отправка электронной почты.
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments:{}'.format(post.title,
                                                                    post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@myblog.com', [cd['to']])
            sent = True
    else:
            form = EmailPostForm()
            return render(request, 'blog/post/share.html',{'post': post, 'form': form, 'sent': sent})

