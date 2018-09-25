from django.conf import settings
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as auth_token
from . import views

router = DefaultRouter()
router.register('todos', views.TodoViewSet)

app_name = 'rest_app'
urlpatterns = [
    path('', TemplateView.as_view(template_name='rest_app/todo_list_vue.html'), name="rest_index/"),
	path('api/', include(router.urls), name='api'),
    path('token/', auth_token.obtain_auth_token, name='token'),
]
