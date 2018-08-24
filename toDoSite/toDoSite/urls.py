"""toDoSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from toDoSite import views

urlpatterns = [
    path('', include('toDoApp.urls')), # include('toDoApp.urls') tells this line to go to urls.py at the all level and tack on those paths after the empty string.
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),#added to use accounts
    path('accounts/register', views.register, name='register'),

]
