
from django.contrib import admin
from django.urls import path, include
from toDoSite import views

# router = routers.DefaultRouter()
# router.register(r'todos', views.TodoViewSet)

urlpatterns = [
    path('', include('toDoApp.urls')), # include('toDoApp.urls') tells this line to go to urls.py at the all level and tack on those paths after the empty string.
    path('rest_index/', include('rest_app.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),#added to use accounts
    path('accounts/register', views.register, name='register'),
	path('api-auth/', include('rest_framework.urls')),

]
