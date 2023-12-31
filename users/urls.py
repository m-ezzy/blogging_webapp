"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views
from .views import login_user, logout_user, account, create_user, display_user, edit_user, delete_user

urlpatterns = [
  path('login/', login_user, name='login_user'),
  path('logout', logout_user, name='logout_user'),

#   path('accounts/profile', account, name='account'),
  path('account/', account, name='account'),

  path("signup", create_user, name="create_user"), # users/create register signup
  path('users/<int:id>', display_user, name='display_user'),
  path('users/<int:id>/edit', edit_user, name='edit_user'),
  path('users/<int:id>/delete', delete_user, name='delete_user'),
]
