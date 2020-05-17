from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_list, name='posts_list_url'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail_url'),
    path('post/create', views.PostCreate.as_view(), name='post_create_url'),
    path('tags/', views.tags_list, name='tags_list_url'),
    path('tag/create', views.TagCreate.as_view(), name='tag_create_url'),
    path('tag/<slug:slug>/', views.TagDetail.as_view(), name='tag_detail'),
    path('tag/<slug:slug>/update/', views.TagUpdate.as_view(), name='tag_update_url'),
    path('post/<slug:slug>/update/', views.PostUpdate.as_view(), name='post_update_url'),
    path('tag/<slug:slug>/delete/', views.TagDelete.as_view(), name='tag_delete_url'),
    path('post/<slug:slug>/delete/', views.PostDelete.as_view(), name='post_delete_url'),

]