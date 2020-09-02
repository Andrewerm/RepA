from django.urls import path
from social_content import views
app_name='social_content'


urlpatterns = [
    path('create/', views.content_create, name='create'),
    path('detail/<int:id>/<slug:slug>', views.content_detail, name='content_details'),
]