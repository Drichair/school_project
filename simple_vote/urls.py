"""simple_vote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='index'),
    path('login/', views.login_page, name='login'),
    path('registration/', views.registr_page, name='registration'),
    path('create/', views.create_page, name='create'),
    path('vote/<int:id>', views.vote_page, name='vote'),
    path('edit/', views.edit_page, name='edit'),
    path('profil/', views.profil_page, name='profil'),
    path('register_done/', views.registr_page, name="registration"),
    path('logout/', views.logout_page, name="logout")
]
