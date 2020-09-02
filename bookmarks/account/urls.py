from django.urls import path
from account import views
from django.contrib.auth.views import PasswordChangeDoneView,PasswordChangeView
app_name='account'

urlpatterns = [
    # path('login/', views.user_login, name='login'),
    path('login/',views.UserLogin.as_view(), name='login'),
    path('logout/',views.UserLogout.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('password_change/',PasswordChangeView.as_view(),name='password_change'),
    path('password_change/done/',PasswordChangeDoneView.as_view(),name='password_change_done'),
]