"""DjangoPizza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from authapp import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('formpage/', views.form_page, name='form-page'),
      path('', views.home, name='home'),
    path('authapp/login', LoginView.as_view(template_name='authapp/login.html'),
         name='authapp-login'),
    path('authapp/logout/', LogoutView.as_view(next_page='/'),
                       name='authapp-logout'),
    path('authapp/', views.authapp_home, name='authapp-home'),
    # path('<int:pizza_id>/', views.pizza_detail, name='pizza-detail'),
    # path('testapp/', include('testurlapp.test_urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+\
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
