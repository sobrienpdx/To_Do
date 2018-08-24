from django.urls import path
from . import views #'.' means this directory- '..' would mean parent

app_name = 'toDoApp'
urlpatterns = [
    path('', views.index, name='index'), #app urls are relative to the paths from urls.py at the site level
    path("add/", views.add, name="add"),
    path("delete/<int:pk>/", views.delete, name="delete"),
    path("mark_done/<int:pk>/", views.mark_done, name="mark_done"),
    path('another_page/', views.another, name='another_page')
]
